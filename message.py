import routine
import xmlparser
import wxresponse


@routine.routine("text")
def msg_text(data):
    try:
        if isinstance(data, xmlparser.TextMsg):
            replyMsg = wxresponse.TextMsg(data.FromUserName,
                                          data.ToUserName,
                                          data.Content
                                          )
            return replyMsg.send()
        else:
            return "success"
    except Exception as e:
        return "error"
