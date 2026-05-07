import streamlit as st
import requests as dat

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "6933682188ce8439fb756dc3e7315e26"

if "progress" not in st.session_state:
    st.session_state.progress = 0
st.set_page_config(
    page_title="Weather app",
    page_icon="☔",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:

    with st.expander("BẢN UPDATE v1.1.2"):
        st.write("+ 1 nhạc")
        st.write("+1 video")
    with st.expander("HƯỚNG DẪN SỬ DỤNG"):
            st.write("Bước 1 : Xác minh bạn có phải người không vì chúng tôi luôn sợ rằng bot sẽ làm lag trang website uy tín của chúng tôi")
            st.write("Bước 2 : Bật nhạc")
            st.write("Bước 3 : hãy điền thành phố mà bạn muốn")
            st.write("Bước 4 : Nhấn nút sumbit để ra kết quả mong muốn")
            st.write("Nếu có thắc mắc hay phàn nàn , hãy liên hệ chúng tôi qua nút report để tư vấn tốt nhất")
            st.write("HÃY SỬ DỤNG VUI VẺ :V")
    st.image("data:image/jpeg;base64,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", caption="cẢM ƠN BẠN ĐÃ SỬ DỤNG")
st.title("                      ⛅WEATHER☔")
st.progress(st.session_state.progress)
argge = st.checkbox("WAIT are you a human ?")
if argge:
    sound = open('Beethoven - Moonlight Sonata 3rd Movement (meganeko Remix).mp3', 'rb')
    st.audio(sound, format='IDK/mp3')
    st.write("GREAT you aren't a human")
    st.balloons()
    with st.form(key= "my form"):
        st.write("City:")
        city = st.text_input("")
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        stu =st.form_submit_button()
        if stu:
            st.balloons()

            try:
                data = dat.get(url).json()

                if str(data["cod"]) == "200":
                    name = data["name"]
                    main = data["weather"][0]["main"]
                    description = data["weather"][0]["description"]
                    temp = data["main"]["temp"]
                    humidity = data["main"]["humidity"]
                    wind_speed = data["wind"]["speed"]

                    st.subheader(name)
                    st.write(f"Main: {main}")
                    st.write(f"Description: {description}")
                    st.write(f"Temperature: {temp}°C")
                    st.write(f"Humidity: {humidity}%")
                    st.write(f"Wind Speed: {wind_speed} m/s")
                    st.video("https://youtu.be/npmlk30wftE?list=RDnpmlk30wftE")
                else:
                    st.error(data["message"])

            except dat.exceptions.RequestException as e:
                print(str(e))


st.write("OI OI OI bạn ơi ")
st.image("https://th.bing.com/th/id/OIP.4ut7TMbKG4qgU62fro2EEQHaEJ?w=307&h=180&c=7&r=0&o=7&pid=1.7&rm=3", caption="LỖI :))")
