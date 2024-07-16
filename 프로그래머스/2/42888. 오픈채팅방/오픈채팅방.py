def solution(record):
    user_nicknames = {}
    events = []

    for entry in record:
        details = entry.split()
        action = details[0]
        uid = details[1]

        if action == "Enter" or action == "Change":
            nickname = details[2]
            user_nicknames[uid] = nickname

        if action == "Enter" or action == "Leave":
            events.append((action, uid))

    result = []
    for action, uid in events:
        if action == "Enter":
            result.append(f"{user_nicknames[uid]}님이 들어왔습니다.")
        elif action == "Leave":
            result.append(f"{user_nicknames[uid]}님이 나갔습니다.")

    return result