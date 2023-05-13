import streamlit as st
from google.cloud import firestore
from PIL import Image
import time


db = firestore.Client.from_service_account_json("firestore-key.json")
st.title('GooYa_GooYa님의 네비게이션')
gooyaimage = Image.open('GooYa_GooYa.png')
col1, col2 = st.columns([1, 2])

with col1:
    st.image(gooyaimage))

with col2:
    st.info("**GooYa_GooYa**")
# Streamlit widgets to let a user create a new post
name = st.text_input("장소 이름")
x = st.text_input("x 좌표")
y = st.text_input("y 좌표")
z = st.text_input("z 좌표")
submit = st.button("확인", key="submit_button")
st.write("---")
# Once the user has submitted, upload it to the database
if name and x and y and z and submit:
    doc_ref = db.collection("path").document(name)
    doc_ref.set({
        "name": name,
        "x": x,
        "y": y,
        "z": z
    })

# And then render each post, using some light Markdown
# And then render each post, using some light Markdown
# Loop through each post and display it
path_ref = db.collection("path")
for doc in path_ref.stream():
    path = doc.to_dict()
    name = path["name"]
    x = path["x"]
    y = path["y"]
    z = path["z"]
    # Display the current values for each post
    st.success(f"Name: {name}")
    st.info(f"x 좌표: {x}")
    st.info(f"y 좌표: {y}")
    st.info(f"z 좌표: {z}")
# Add a delete button
    delete_button = st.button(f"삭제하기", key=f"delete_{doc.id}")
    if delete_button:
        doc_ref = db.collection("path").document(name)
        doc_ref.delete()
        st.experimental_rerun()

    pathstart = st.button("출발", key=doc.id)
    if pathstart:
        pathstop = st.button("중지", key=f"pathdelete")
        from mcpi.minecraft import Minecraft
        mc = Minecraft.create()  # 마인크래프트에 연결
        while True:
            player_ids = mc.getPlayerEntityIds()
            pos = mc.entity.getTilePos(player_ids[1])
            X_AXIS = 65
            Y_AXIS = 63
            Z_AXIS = 146
            pos_x = pos.x + X_AXIS
            pos_y = pos.y + Y_AXIS
            pos_z = pos.z + Z_AXIS
            mc.postToChat("GooYa Position: x={0} y={1} z={2}".format(
                str(x-pos_x), str(y-pos_y), str(z-pos_z)))
            time.sleep(1)
            if pathstop:
                break
