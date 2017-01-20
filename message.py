import routine
import xmlparser
import wxresponse


@routine.routine("/wx")
def msg_text(text):
    try:
        if isinstance(text, xmlparser.TextMsg):
            replyMsg = wxresponse.TextMsg(text.ToUserName,
                                          text.FromUserName,
                                          text.Content,
                                          )
            return replyMsg.send()
        else:
            return "success"
    except Exception as e:
        return "error"
