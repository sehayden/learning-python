lohen_log = []
hati_log = []
please_count = 1
conversation_to_view = ""


def lohen_challenges_hati():
    global please_count, conversation_to_view
    while "stop" not in hati_log and  "ok" not in hati_log :
        lohen_line = "please " * please_count + "fight me"
        print(f"Lohen: {lohen_line}")
        lohen_log.append(lohen_line)

        hati_line = input("Hati: ")
        print(f"Hati: {hati_line}")
        hati_log.append(hati_line)

        please_count += 1

    conversation_to_view = input("L to view Lohen's, H to view Hati's, else view all: ")
    view_conversation(conversation_to_view)
    
def view_conversation(conversation_to_view):
    if (conversation_to_view == "L"):
        for log in lohen_log:
            print(f"Lohen: {log}")
    elif (conversation_to_view == "H"):
        for log in hati_log:
            print(f"Hati: {log}")
    else:
        for i in range(0, len(lohen_log)):
            print(f"Lohen: {lohen_log[i]}")
            print(f"Hati: {hati_log[i]}")


lohen_challenges_hati()