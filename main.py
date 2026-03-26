import streamlit as st
import cv2
import numpy as np

st.set_page_config(layout="wide", page_title="IMGorithm")


st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 10%, rgba(0,255,195,0.08), transparent 40%),
                radial-gradient(circle at 80% 20%, rgba(0,180,255,0.08), transparent 40%),
                #020b12;
}
.block-container {
    padding-top: 20px !important;
            }
.title-wrap {
    margin-top: 20px;
    margin-bottom: 30px;
}

.main-title {
    font-size: 3.2rem;
    font-weight: 800;
    color: #e2f5f0;
    letter-spacing: -1px;
}

.main-title span {
    color: #00ffc3;
}

.sub-title {
    font-size: 1rem;
    color: #6ea8a0;
    margin-top: 8px;
}


.glass-card {
    background: rgba(255,255,255,0.04);
    border-radius: 20px;
    padding: 20px 25px;   /* reduce top padding */
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}
            

.stButton > button {
    background: linear-gradient(135deg,#00ffc3,#00b4ff) !important;
    color: black !important;
    border-radius: 10px !important;
}

/* Section Titles */
.section-title {
    color: #00ffc3;
    font-size: 0.8rem;
    margin-top: 15px;
}

/* Preview */
.preview-box {
    height: 520px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg,#0d2a26,#0a1f2e,#1a0a2e);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 40px rgba(0,255,195,0.1);
}

.preview-header {
    color: #00ffc3;
    font-size: 1.2rem;
}

/* Footer */
.footer {
    margin-top: 40px;
    padding: 20px 40px;
    border-top: 1px solid rgba(255,255,255,0.08);
    display: flex;
    justify-content: space-between;
    color: #6ea8a0;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-wrap">
    <div class="main-title">IMG<span>orithm</span></div>
    <div class="sub-title">
        Where images meet algorithms — fast, clean, and powerful image processing
    </div>
</div>
""", unsafe_allow_html=True)


keys = ["show","resize","grey","blur","lap","sobel","canny",
        "rotate_cw","rotate_ccw","rotate_180","warm","sharpen",
        "brightness","portrait"]

for k in keys:
    if k not in st.session_state:
        st.session_state[k] = False

def reset():
    for k in keys:
        st.session_state[k] = False


col1, col2 = st.columns([4,2])

img = None
output = None

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])
    if st.button("Show Original"):
        reset()
        st.session_state["show"] = True

    st.markdown('<div class="section-title">Resize</div>', unsafe_allow_html=True)
    h = st.number_input("Height", 1, 2000, 600)
    w = st.number_input("Width", 1, 2000, 600)
    if st.button("Apply Resize"): reset(); st.session_state["resize"]=True

    st.markdown('<div class="section-title">Filters</div>', unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    if c1.button("Greyscale"): reset(); st.session_state["grey"]=True
    if c2.button("Warm"): reset(); st.session_state["warm"]=True
    if c3.button("Sharpen"): reset(); st.session_state["sharpen"]=True

    st.markdown('<div class="section-title">Edges</div>', unsafe_allow_html=True)
    e1,e2,e3 = st.columns(3)
    if e1.button("Laplacian"): reset(); st.session_state["lap"]=True
    if e2.button("Canny"): reset(); st.session_state["canny"]=True
    if e3.button("Sobel"): reset(); st.session_state["sobel"]=True

    st.markdown('<div class="section-title">Blur</div>', unsafe_allow_html=True)
    blur_k = st.slider("Blur",1,25,5)
    if st.button("Apply Blur"): reset(); st.session_state["blur"]=True

    st.markdown('<div class="section-title">Brightness & Contrast</div>', unsafe_allow_html=True)
    brightness = st.slider("Brightness",-100,100,0)
    contrast = st.slider("Contrast",0.5,3.0,1.0)
    if st.button("Apply BC"): reset(); st.session_state["brightness"]=True

    st.markdown('<div class="section-title">Portrait Blur</div>', unsafe_allow_html=True)
    p_blur = st.slider("Strength",1,51,21)
    if st.button("Portrait Blur"): reset(); st.session_state["portrait"]=True

    st.markdown('<div class="section-title">Rotate</div>', unsafe_allow_html=True)
    r1,r2,r3 = st.columns(3)
    if r1.button("90 CW"): reset(); st.session_state["rotate_cw"]=True
    if r2.button("90 CCW"): reset(); st.session_state["rotate_ccw"]=True
    if r3.button("180"): reset(); st.session_state["rotate_180"]=True

    st.markdown('</div>', unsafe_allow_html=True)

with col1:
    #st.markdown('<div class="glass-card"></div>', unsafe_allow_html=True)
    st.markdown('<div class="preview-header">Preview</div>', unsafe_allow_html=True)

    if file:
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if st.session_state["resize"]:
            if w < img.shape[1] or h < img.shape[0]:
                # Downscale → use INTER_AREA (sharp + best)
                img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
            else:
                # Upscale → use INTER_CUBIC (better quality)
                img = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)

        if st.session_state["grey"]:
            output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        elif st.session_state["blur"]:
            output = cv2.GaussianBlur(img,(blur_k,blur_k),1)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        elif st.session_state["lap"]:
            output = cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),-1)

        elif st.session_state["sobel"]:
            output = cv2.Sobel(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),-1,1,0)

        elif st.session_state["canny"]:
            output = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),50,150)

        elif st.session_state["rotate_180"]:
            output = cv2.rotate(img, cv2.ROTATE_180)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        elif st.session_state["rotate_cw"]:
            output = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        elif st.session_state["rotate_ccw"]:
            output = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        elif st.session_state["sharpen"]:
            kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
            output = cv2.filter2D(img,-1,kernel)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        elif st.session_state["warm"]:
            temp = img.copy()
            temp[:,:,2]+=30
            output = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)

        elif st.session_state["brightness"]:
            output = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        elif st.session_state["portrait"]:
            h1,w1 = img.shape[:2]
            mask = np.zeros((h1,w1),dtype=np.uint8)
            cv2.ellipse(mask,(w1//2,h1//2),(int(w1*0.4),int(h1*0.5)),0,0,360,255,-1)
            blur = cv2.GaussianBlur(img,(p_blur,p_blur),0)
            mask = cv2.GaussianBlur(mask,(51,51),0)/255
            output = (img*mask[:,:,None] + blur*(1-mask[:,:,None])).astype(np.uint8)
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

        else:
            output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        st.image(output, use_container_width=True)

        if len(output.shape) == 2:
            download_img = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
        else:
            download_img = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

        _, buffer = cv2.imencode('.png', download_img)
        st.download_button("Download Image", buffer.tobytes(), "imgorithm.png")

    else:
        st.markdown('<div class="preview-box">Upload image to start</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div>© 2026 IMGorithm</div>
    <div>v2.0 Stable</div>
</div>
""", unsafe_allow_html=True)
