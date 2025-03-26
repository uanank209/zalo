import os
import importlib
import math
from zlapi.models import Message, MultiMsgStyle, MessageStyle
des = {"version": "1.0.2", "credits": "Hiển", "description": "welcomeImg"}
def get_all_mitaizl():
    mitaizl = {}
    for module_name in os.listdir('modules'):
        if module_name.endswith('.py') and module_name != '__init__.py':
            module_path = f'modules.{module_name[:-3]}'
            module = importlib.import_module(module_path)
            if hasattr(module, 'get_mitaizl'):
                module_mitaizl = module.get_mitaizl()
                mitaizl.update(module_mitaizl)
    return list(mitaizl.keys())

def handle_menu_command(message, message_object, thread_id, thread_type, author_id, client):
    command_names = get_all_mitaizl()
    total_commands = len(command_names)
    items_per_page = 10
    total_pages = math.ceil(total_commands / items_per_page)
    
    try:
        page_number = int(message.split()[1]) if len(message.split()) > 1 else 1
    except ValueError:
        page_number = 1

    page_number = max(1, min(total_pages, page_number))
    start_index = (page_number - 1) * items_per_page
    end_index = min(start_index + items_per_page, total_commands)
    paged_commands = command_names[start_index:end_index]

    numbered_mitaizl = [f"{i + 1 + start_index}. {name}" for i, name in enumerate(paged_commands)]
    menu_message = (
        f"==== [ 𝕄𝕖𝕟𝕦 ℂ𝕦̉𝕒 𝔹𝕠𝕥 ] ====\n"
        f"🌟 ℂ𝕙𝕦̉ ℕ𝕙𝕒̂𝕟 : HNguyen\n"
        f"👑 𝔸𝕕𝕞𝕚𝕟 : HNguyen\n"
        f"📋 𝕋𝕠̂̉𝕟𝕘 𝕤𝕠̂́ 𝕝𝕖̣̂𝕟𝕙 : {total_commands}\n"
        "" + "\n".join(numbered_mitaizl) + "\n"
        f"𝕋𝕣𝕒𝕟𝕘 {page_number}/{total_pages}"
        f" :𝔻𝕦𝕟𝕘 𝕝𝕖̣̂𝕟𝕙 𝕞𝕖𝕟𝕦 <𝕤𝕠̂́_𝕥𝕣𝕒𝕟𝕘> 𝕕𝕖̂̉ 𝕔𝕙𝕦𝕪𝕖̂̉𝕟 𝕥𝕣𝕒𝕟𝕘."
    )

    msg_length = len(menu_message)
    style = MultiMsgStyle([
        MessageStyle(offset=0, length=msg_length, style="color", color="40ff00", auto_format=False),
        MessageStyle(offset=0, length=msg_length, style="sansserif", auto_format=False)
    ])
    message_to_send = Message(text=menu_message, style=style)
    client.replyMessage(message_to_send, message_object, thread_id, thread_type)

def get_mitaizl():
    return {
        'menu': handle_menu_command
    }