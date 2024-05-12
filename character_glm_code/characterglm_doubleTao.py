import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response


def characterglm_example():
    character_meta = {
        "user_info": "",
        "bot_info": "doubleTao，性别男，28岁，在大公司担任IT技术工程师。doubleTao性格孤僻，加班较多。经常失恋。最近doubleTao又和女朋友因为加班原因分手了，心情很差。同事小梅经常在失恋后安慰他，并给他讲解如何与女孩子相处恋爱",
        "user_name": "用户",
        "bot_name": "doubleTao"
    }
    messages = [
        {"role": "assistant", "content": "doubleTao，分手很正常，一定会找到更适合的人的，加油"},
        {"role": "user", "content": "谢谢小梅，每次和你聊天后都会非常开心，没有负担了"}
    ]
    for chunk in get_characterglm_response(messages, meta=character_meta):
        print(chunk)
        time.sleep(0.5)


if __name__ == "__main__":
    characterglm_example()
