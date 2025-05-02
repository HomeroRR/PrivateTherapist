# hello_world_search.py
#
# 1) Upload “Hello World!” as raw content
# 2) Ask the workspace what the file says

import os, requests, time

API = "https://sdk.senso.ai/api/v1"
HDR = {"X-API-Key": os.environ["SENSO_KEY"]}

# 1) SOURCE – upload raw text
hello_txt = "Mike is a 20 year-old who reports to you that he feels depressed and is experiencing a significant amount of stress about school, noting that he’ll “probably flunk out.” He spends much of his day in his dorm room playing video games and has a hard time identifying what, if anything, is enjoyable in a typical day. He rarely attends class and has avoided reaching out to his professors to try to salvage his grades this semester. Mike has always been a self-described shy person and has had a very small and cohesive group of friends from elementary through high school. Notably, his level of stress significantly amplified when he began college. You learn that when meeting new people, he has a hard time concentrating on the interaction because he is busy worrying about what they will think of him – he assumes they will find him “dumb,” “boring,” or a “loser.” When he loses his concentration, he stutters, is at a loss for words, and starts to sweat, which only serves to make him feel more uneasy. After the interaction, he replays the conversation over and over again, focusing on the “stupid” things he said. Similarly, he has a long-standing history of being uncomfortable with authority figures and has had a hard time raising his hand in class and approaching teachers. Since starting college, he has been isolating more, turning down invitations from his roommate to go eat or hang out, ignoring his cell phone when it rings, and habitually skipping class. His concerns about how others view him are what drive him to engage in these avoidance behaviors. After conducting your assessment, you give the patient feedback that you believe he has social anxiety disorder, which should be the primary treatment target. You explain that you see his fear of negative evaluation, and his thoughts and behaviors surrounding social situations, as driving his increasing sense of hopelessness, isolation, and worthlessness."
content = requests.post(
    f"{API}/content/raw",
    headers=HDR,
    json={"title": "hello.txt", "text": hello_txt}
).json()
cid = content["id"]
print("Uploaded content_id →", cid)

# (wait until processing is done – usually a few seconds)
while content["processing_status"] != "completed":
    time.sleep(2)
    content = requests.get(f"{API}/content/{cid}", headers=HDR).json()

# 2) WORKSPACE – ask a question
answer = requests.post(
    f"{API}/search",
    headers=HDR,
    json={"query": "What is the severity?"}
).json()

print("\nAI answer →", answer["answer"])
print("\nFirst cited source →", answer["results"][0]["chunk_text"])