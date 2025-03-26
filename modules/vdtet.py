from zlapi.models import Message
import requests

des = {
    'version': "1.0.2",
    'credits': "𝙦𝙪𝙖𝙣𝙜 𝙫𝙪̃",
    'description': "Gửi video tết"
}

def handle_vdtet_command(message, message_object, thread_id, thread_type, author_id, client):
    uptime_message = "Video Anime của bạn đây."
    message_to_send = Message(text=uptime_message)
    
    api_url = 'https://apiquockhanh.click/video/videotet'
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        video_url = data.get('url', '')
        thumbnail_url = 'https://i.imgur.com/BuvmnYs.mp4'
        duration = '1000'

        # Lấy tên người dùng hoặc dùng author_id
        caller_name = getattr(message_object, 'sender_name', None) or author_id
        
        client.sendRemoteVideo(
            video_url, 
            thumbnail_url,
            duration=duration,
            message=Message(text=f"Video Tết Của You Đây ☝️ "),
            thread_id=thread_id,
            thread_type=thread_type,
            ttl=1200000,
            width=1080,
            height=1920
        )
        
    except requests.exceptions.RequestException as e:
        error_message = Message(text=f"Đã xảy ra lỗi khi gọi API: {str(e)}")
        client.sendMessage(error_message, thread_id, thread_type, ttl=1000)
    except Exception as e:
        error_message = Message(text=f"Đã xảy ra lỗi: {str(e)}")
        client.sendMessage(error_message, thread_id, thread_type, ttl=1000)

def get_mitaizl():
    return {
        'vdtet': handle_vdtet_command
    }
