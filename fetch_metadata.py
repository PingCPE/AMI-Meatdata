import boto3
import json
from datetime import datetime
import argparse


class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON Encoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO 8601 string
        return super().default(obj)


def fetch_instance_metadata(instance_id, data_key=None):
    """Fetch metadata for a specific EC2 instance."""
    # Initialize Boto3 EC2 client
    ec2_client = boto3.client("ec2")

    try:
        # Describe the target instance
        response = ec2_client.describe_instances(InstanceIds=[instance_id])

        # Parse the metadata of the first instance in the response
        instance_metadata = response["Reservations"][0]["Instances"][0]

        if data_key:
            # Retrieve a specific key from metadata if provided
            if data_key in instance_metadata:
                return {data_key: instance_metadata[data_key]}
            else:
                raise KeyError(f"Key '{data_key}' not found in instance metadata.")
        return instance_metadata

    except Exception as e:
        raise RuntimeError(f"Failed to fetch instance metadata: {str(e)}")


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Fetch metadata for an AWS EC2 instance.")
    parser.add_argument(
        "--instance-id", 
        required=True, 
        help="The ID of the EC2 instance to fetch metadata for."
    )
    parser.add_argument(
        "--data-key", 
        help="Optional key to fetch specific metadata (e.g., 'InstanceType')."
    )
    args = parser.parse_args()

    try:
        # Fetch instance metadata
        metadata = fetch_instance_metadata(args.instance_id, args.data_key)

        # Print metadata as JSON
        print(json.dumps(metadata, indent=4, cls=DateTimeEncoder))

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
