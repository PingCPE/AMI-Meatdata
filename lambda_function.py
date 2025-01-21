import boto3
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON Encoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to ISO 8601 string
        return super().default(obj)

def lambda_handler(event, context):
    """Lambda handler function."""
    # Initialize Boto3 EC2 client
    ec2_client = boto3.client("ec2")

    # Replace '<instance-id>' with the instance ID you want to query
    # Use event.get("instance_id") to dynamically fetch instance ID if provided
    target_instance_id = event.get("instance_id", "i-04d27291150792ee5")

    try:
        # Describe the target instance
        response = ec2_client.describe_instances(InstanceIds=[target_instance_id])

        # Parse the metadata of the first instance in the response
        instance_metadata = response["Reservations"][0]["Instances"][0]

        # Return the metadata as a formatted JSON response with custom encoder
        return {
            "statusCode": 200,
            "body": json.dumps(instance_metadata, indent=4, cls=DateTimeEncoder)
        }
    except Exception as e:
        # Handle errors gracefully
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
