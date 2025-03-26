from zlapi.models import Message
import requests
import random
import json
import ffmpeg

des = {
    'version': "1.0.2",
    'credits': "Nguyễn Đức Tài",
    'description': "Gửi video chill"
}

def get_video_info(video_url):
    try:
        probe = ffmpeg.probe(video_url)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        
        if video_stream:
            duration = float(video_stream['duration']) * 1000
            width = int(video_stream['width'])
            height = int(video_stream['height'])
            return duration, width, height
        else:
            raise Exception("Không tìm thấy luồng video trong URL")
    except Exception as e:
        raise Exception(f"Lỗi khi lấy thông tin video: {str(e)}")

def handle_vdchill_command(message, message_object, thread_id, thread_type, author_id, client):    
    try:
        with open("modules/cache/data/vdchill.json", "r") as video_file:
            video_urls = json.load(video_file)
        
        video_url = random.choice(video_urls)
        image_url = "https://f57-zpg-r.zdn.vn/jpg/693221116131739333/c12347bbcadc718228cd.jpg"

        duration, width, height = get_video_info(video_url)

        client.sendRemoteVideo(
            video_url, 
            image_url,
            duration=int(duration),
            message=None,
            thread_id=thread_id,
            thread_type=thread_type,
            width=width,
            height=height
        )

    except requests.exceptions.RequestException as e:
        error_message = Message(text=f"Đã xảy ra lỗi khi gọi API: {str(e)}")
        client.sendMessage(error_message, thread_id, thread_type)
    except Exception as e:
        error_message = Message(text=f"Đã xảy ra lỗi: {str(e)}")
        client.sendMessage(error_message, thread_id, thread_type)

def get_mitaizl():
    return {
        'vdchill': handle_vdchill_command
    }
