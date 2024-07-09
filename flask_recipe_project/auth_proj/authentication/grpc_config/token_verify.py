import jwt
import logging


def token_verification(auth_token):
    """
    Method to verify the access token and extract user ID and success flag.

    Args:
        auth_token: The auth token received from the gRPC request.

    Returns:
        dict(bool, int): A dict containing success flag (True/False) and user ID (0 for failure).
    """
    data = {
        "success": False,
        "user_id": 0,
    }

    
    if not auth_token:
        logging.warning("Token not provided in request.")
        return data["success"], data["user_id"]

    try:

        # Manually decode the JWT token using secret key (replace with your logic)
        secret_key = "helloworld"
        decoded_data = jwt.decode(auth_token, secret_key, algorithms=["HS256"])

        #Get user_id from decoded data(payload)
        user_id = decoded_data.get("sub", {}).get("user_id", 0)
        
        #Update data to true and respective user_id
        data.update({"success": True, "user_id": user_id})
        return data["success"], data["user_id"]

    #Exception Handling:
    
    except jwt.ExpiredSignatureError:
        logging.error("Unauthorized. Expired authentication token.")
        data["message"] = "Unauthorized. Invalid authentication token."
        return data["success"], data["user_id"]

    except jwt.InvalidTokenError:
        logging.error("Unauthorized. Invalid authentication token.")
        return data["success"], data["user_id"]

    except Exception as e:
        logging.error(
            "token_verification - Error while verifying auth token. Error: %s",
            str(e),
            exc_info=True,
        )
        return data["success"], data["user_id"]
