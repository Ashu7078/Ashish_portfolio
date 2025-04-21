import streamlit as st
import json
from PIL import Image

# Load JSON Data with Error Handling
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"projects": [], "blogs": [], "resume": {"link": "#"}}

def main():
    st.set_page_config(page_title="Ashish's Portfolio", layout="wide")

    # Load Image with Error Handling
    try:
        image = Image.open("your_image.jpg")  # Replace with your actual image
    except FileNotFoundError:
        image = None

    # Load Portfolio Data
    data = load_data()

    # Apply Enhanced Custom CSS for Cyberpunk-Themed Portfolio
    st.markdown(
        """
        <style>
            /* Base Cyberpunk Theme */
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
            
            @keyframes neonGlow {
                0% { box-shadow: 0 0 5px #0ff, 0 0 10px #0ff; text-shadow: 0 0 5px #0ff; }
                50% { box-shadow: 0 0 20px #ff00ff, 0 0 30px #ff00ff; text-shadow: 0 0 10px #ff00ff; }
                100% { box-shadow: 0 0 5px #0ff, 0 0 10px #0ff; text-shadow: 0 0 5px #0ff; }
            }
            
            @keyframes glitchEffect {
                0% { transform: translate(0); }
                20% { transform: translate(-2px, 2px); }
                40% { transform: translate(-2px, -2px); }
                60% { transform: translate(2px, 2px); }
                80% { transform: translate(2px, -2px); }
                100% { transform: translate(0); }
            }
            
            @keyframes scanline {
                0% { transform: translateY(-100%); }
                100% { transform: translateY(100%); }
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            @keyframes backgroundPulse {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            @keyframes flicker {
                0% { opacity: 0.8; }
                5% { opacity: 0.5; }
                10% { opacity: 0.9; }
                15% { opacity: 0.6; }
                20% { opacity: 0.8; }
                25% { opacity: 1; }
                30% { opacity: 0.6; }
                35% { opacity: 0.9; }
                40% { opacity: 0.7; }
                45% { opacity: 0.9; }
                50% { opacity: 0.8; }
                100% { opacity: 1; }
            }
            
            @keyframes borderGlow {
                0% { border-color: #0ff; }
                50% { border-color: #ff00ff; }
                100% { border-color: #0ff; }
            }
            
            /* Apply to entire app */
            body, .stApp, .block-container, header {
                font-family: 'Share Tech Mono', monospace !important;
                background-color: #0c0c16 !important;
                color: #0ff !important;
                background-image: 
                    linear-gradient(0deg, rgba(12,12,22,0.9), rgba(12,12,22,0.9)), 
                    url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="none" stroke="%230ff" stroke-width="0.5" stroke-dasharray="5,5" /></svg>');
            }
            
            /* Add scanline effect across the entire app */
            body::before {
                content: "";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 5px;
                background: rgba(0, 255, 255, 0.2);
                z-index: 1000;
                animation: scanline 8s linear infinite;
                pointer-events: none;
            }
            
            /* Enhanced sidebar */
            div[data-testid='stSidebar'], div[data-testid='stSidebarNav'] {
                background-color: #080812 !important;
                color: #0ff !important;
                border-right: 2px solid #0ff;
                box-shadow: 0 0 15px #0ff;
                animation: borderGlow 4s infinite alternate;
            }
            
            div[data-testid='stSidebarContent'] {
                background-color: #080812 !important;
            }
            
            /* Enhanced Radio Buttons (Navigation) */
            .st-cc, .st-c0, .st-bZ, .st-ca {
                color: #ff00ff !important;
                font-family: 'Orbitron', sans-serif !important;
                font-weight: bold !important;
                animation: neonGlow 3s infinite alternate;
            }
            
            /* Selected radio button */
            .st-bd {
                background-color: #ff00ff !important;
            }
            
            /* Cyberpunk Buttons */
            div.stButton > button {
                background: linear-gradient(90deg, #0ff, #ff00ff) !important;
                color: #000 !important;
                font-family: 'Orbitron', sans-serif !important;
                font-weight: bold !important;
                border: none !important;
                border-radius: 8px !important;
                padding: 12px 24px !important;
                transition: all 0.3s ease-in-out !important;
                position: relative !important;
                overflow: hidden !important;
                animation: neonGlow 2s infinite alternate !important;
                text-transform: uppercase !important;
                letter-spacing: 2px !important;
            }
            
            div.stButton > button:hover {
                transform: scale(1.05) !important;
                box-shadow: 0 0 25px #ff00ff, 0 0 35px #0ff !important;
                animation: glitchEffect 0.3s infinite !important;
            }
            
            div.stButton > button:active {
                transform: scale(0.95) !important;
            }
            
            /* Enhanced Titles */
            h1, h2, h3 {
                font-family: 'Orbitron', sans-serif !important;
                text-align: center !important;
                color: #0ff !important;
                text-shadow: 0 0 10px #0ff, 0 0 20px #0ff !important;
                animation: flicker 2s infinite alternate, fadeIn 1.5s ease-in-out !important;
                letter-spacing: 3px !important;
                margin-bottom: 30px !important;
                position: relative !important;
            }
            
            h1::after, h2::after {
                content: "";
                position: absolute;
                bottom: -10px;
                left: 50%;
                transform: translateX(-50%);
                width: 60%;
                height: 2px;
                background: linear-gradient(90deg, transparent, #0ff, #ff00ff, #0ff, transparent);
            }
            
            /* Enhanced Text */
            p, li, a {
                font-family: 'Share Tech Mono', monospace !important;
                letter-spacing: 1px !important;
                line-height: 1.6 !important;
                animation: fadeIn 1s ease-in-out !important;
            }
            
            /* Links */
            a {
                color: #ff00ff !important;
                text-decoration: none !important;
                transition: all 0.3s ease !important;
                position: relative !important;
                display: inline-block !important;
            }
            
            a:hover {
                color: #0ff !important;
                text-shadow: 0 0 8px #0ff !important;
            }
            
            a:hover::after {
                content: "";
                position: absolute;
                bottom: -2px;
                left: 0;
                width: 100%;
                height: 1px;
                background: #0ff;
                box-shadow: 0 0 8px #0ff;
                animation: neonGlow 1.5s infinite alternate;
            }
            
            /* Form inputs */
            .stTextInput > div > div > input, .stTextArea > div > div > textarea {
                background-color: rgba(0, 0, 0, 0.7) !important;
                color: #0ff !important;
                border: 1px solid #0ff !important;
                border-radius: 8px !important;
                box-shadow: 0 0 5px #0ff !important;
                font-family: 'Share Tech Mono', monospace !important;
                transition: all 0.3s ease !important;
            }
            
            .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
                box-shadow: 0 0 15px #ff00ff !important;
                border-color: #ff00ff !important;
            }
            
            /* Dividers */
            hr {
                border: 0 !important;
                height: 2px !important;
                background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,255,255,0.75), rgba(255,0,255,0.75), rgba(0,255,255,0.75), rgba(0,0,0,0)) !important;
                animation: backgroundPulse 5s infinite linear !important;
                background-size: 200% 200% !important;
                margin: 25px 0 !important;
            }
            
            /* Project and Blog cards */
            div.element-container:has(h3) {
                border: 1px solid #0ff !important;
                border-radius: 10px !important;
                padding: 15px !important;
                margin-bottom: 20px !important;
                box-shadow: 0 0 10px #0ff !important;
                transition: all 0.3s ease !important;
                animation: borderGlow 4s infinite alternate !important;
                background: linear-gradient(135deg, rgba(0,0,0,0.7), rgba(0,30,60,0.3)) !important;
            }
            
            div.element-container:has(h3):hover {
                transform: translateY(-5px) !important;
                box-shadow: 0 0 20px #ff00ff !important;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 12px !important;
                height: 12px !important;
            }
            
            ::-webkit-scrollbar-track {
                background: #0c0c16 !important;
                border-left: 1px solid rgba(0, 255, 255, 0.3) !important;
            }
            
            ::-webkit-scrollbar-thumb {
                background: linear-gradient(180deg, #0ff, #ff00ff) !important;
                border-radius: 6px !important;
                border: 2px solid #0c0c16 !important;
                box-shadow: 0 0 8px rgba(0, 255, 255, 0.5) !important;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: linear-gradient(180deg, #ff00ff, #0ff) !important;
            }
            
            /* Footer */
            footer {
                position: relative !important;
                padding-top: 20px !important;
                border-top: 2px solid #0ff !important;
                animation: borderGlow 4s infinite alternate !important;
            }
            
            footer p {
                animation: flicker 2s infinite alternate !important;
                font-family: 'Orbitron', sans-serif !important;
                text-align: center !important;
            }
            
            /* Animated Background for Home */
            .cyber-bg {
                position: relative !important;
                overflow: hidden !important;
                padding: 20px !important;
                border-radius: 15px !important;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
                animation: fadeIn 1s ease-in-out !important;
                background: 
                    linear-gradient(135deg, rgba(0,0,0,0.9) 0%, rgba(20,20,40,0.8) 100%),
                    url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200"><rect width="200" height="200" fill="none" stroke="%230ff" stroke-width="1" stroke-dasharray="10,10" /></svg>') !important;
            }
            
            /* Projects and Blog animations */
            .cyber-card {
                position: relative !important;
                overflow: hidden !important;
                animation: fadeIn 1s ease-in-out !important;
            }
            
            .cyber-card::before {
                content: "" !important;
                position: absolute !important;
                top: -50% !important;
                left: -50% !important;
                width: 200% !important;
                height: 200% !important;
                background: linear-gradient(45deg, transparent, rgba(0, 255, 255, 0.2), transparent) !important;
                transform: rotate(45deg) !important;
                animation: scanline 3s linear infinite !important;
                z-index: -1 !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar Navigation with Enhanced Cyberpunk Styling
    menu = ["Home", "My Projects", "My Blogs", "My Resume", "About Me", "Contact Me"]
    icons = {"Home": "🏠", "My Projects": "📂", "My Blogs": "✍️", "My Resume": "📄", "About Me": "ℹ️", "Contact Me": "📞"}
    
    # Create custom styled sidebar title
    st.sidebar.markdown("<h2 style='text-align: center; color: #ff00ff; text-shadow: 0 0 10px #ff00ff; font-family: Orbitron, sans-serif;'>NAVIGATE</h2>", unsafe_allow_html=True)
    
    # Add animated divider
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    
    choice = st.sidebar.radio("", menu, format_func=lambda x: f"{icons[x]} {x}")
    
    # Add animated social links to sidebar
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 10px; margin-top: 30px; animation: fadeIn 2s ease-in-out;'>
        <p style='font-family: "Orbitron", sans-serif; color: #0ff; text-shadow: 0 0 5px #0ff;'>CONNECT</p>
        <a href='https://github.com/' style='margin: 0 10px; font-size: 24px;' title='GitHub'>🔗</a>
        <a href='https://linkedin.com/' style='margin: 0 10px; font-size: 24px;' title='LinkedIn'>📱</a>
        <a href='https://twitter.com/' style='margin: 0 10px; font-size: 24px;' title='Twitter'>🐦</a>
    </div>
    """, unsafe_allow_html=True)

    # Main Content with Enhanced Styling
    container = st.container()
    with container:
        if choice == "Home":
            st.markdown("<h1 style='animation: flicker 2s infinite alternate, glitchEffect 5s infinite;'>ASHISH'S CYBERPUNK PORTFOLIO</h1>", unsafe_allow_html=True)
            
            # Animated intro section
            st.markdown("""
            <div class='cyber-bg'>
                <p style='font-size: 18px; text-align: center; animation: fadeIn 2s ease-in-out;'>
                    <span style='color: #ff00ff; font-weight: bold;'>WELCOME TO MY DIGITAL REALM</span>
                </p>
                <p style='text-align: center; animation: fadeIn 3s ease-in-out;'>
                    I'm Ashish, a <span style='color: #ff00ff; text-shadow: 0 0 5px #ff00ff;'>data analyst</span> exploring the power of data in a tech-driven world.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("""
                <div style='animation: fadeIn 2s ease-in-out;'>
                    <h3>SKILLSET</h3>
                    <ul>
                        <li>Data Analysis & Visualization</li>
                        <li>Machine Learning</li>
                        <li>Python Programming</li>
                        <li>SQL & Database Management</li>
                        <li>Web Development</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                # Call-to-action buttons with animation
                col1_1, col1_2 = st.columns(2)
                with col1_1:
                    st.button("View Projects")
                with col1_2:
                    st.button("Contact Me")
                
            with col2:
                if image:
                    st.image(image, width=250)
                else:
                    # Placeholder SVG if no image is available
                    st.markdown("""
                    <div style='text-align: center; padding: 20px; border: 2px solid #ff00ff; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; animation: borderGlow 4s infinite alternate, fadeIn 2s ease-in-out;'>
                        <svg width="150" height="150" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="50" cy="35" r="20" fill="none" stroke="#0ff" stroke-width="2" />
                            <path d="M30,70 Q50,90 70,70" fill="none" stroke="#0ff" stroke-width="2" />
                        </svg>
                    </div>
                    """, unsafe_allow_html=True)

        elif choice == "My Projects":
            st.markdown("<h1>MY PROJECTS</h1>", unsafe_allow_html=True)
            
            # Introduction text with animation
            st.markdown("""
            <p style='text-align: center; margin-bottom: 30px; animation: fadeIn 1s ease-in-out;'>
                Explore my digital creations and data-driven projects in the cybernetic landscape.
            </p>
            """, unsafe_allow_html=True)
            
            # Show projects with enhanced styling
            for i, project in enumerate(data.get("projects", [])):
                # Alternate colors for adjacent projects
                color_accent = "#0ff" if i % 2 == 0 else "#ff00ff"
                
                st.markdown(f"""
                <div class='cyber-card' style='border-left: 3px solid {color_accent}; padding-left: 15px; margin-bottom: 25px; animation: fadeIn {1 + i*0.2}s ease-in-out;'>
                    <h3 style='color: {color_accent}; text-shadow: 0 0 5px {color_accent};'>{project.get("title", "Untitled")}</h3>
                    <p>{project.get("description", "No description available.")}</p>
                    <p style='margin-top: 10px;'>
                        <a href='{project.get("github", "#")}' target='_blank' style='background: linear-gradient(90deg, #0c0c16, {color_accent}22); padding: 5px 10px; border-radius: 5px; display: inline-block;'>
                            <span style='margin-right: 5px;'>🔗</span> GitHub Repository
                        </a>
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
            # If no projects, show an animated empty state
            if not data.get("projects", []):
                st.markdown("""
                <div style='text-align: center; padding: 40px; border: 1px dashed #0ff; border-radius: 10px; animation: borderGlow 4s infinite alternate, fadeIn 1s ease-in-out;'>
                    <p style='color: #0ff; font-size: 18px;'>No projects available yet. Check back soon!</p>
                </div>
                """, unsafe_allow_html=True)

        elif choice == "My Blogs":
            st.markdown("<h1>MY BLOGS</h1>", unsafe_allow_html=True)
            
            # Introduction for blogs section
            st.markdown("""
            <p style='text-align: center; margin-bottom: 30px; animation: fadeIn 1s ease-in-out;'>
                Thoughts and insights from the digital frontier.
            </p>
            """, unsafe_allow_html=True)
            
            # Show blogs with enhanced styling
            for i, blog in enumerate(data.get("blogs", [])):
                # Calculate animation delay based on index
                delay = 0.5 + (i * 0.2)
                
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #0c0c1600, #0c0c1644); border-radius: 10px; padding: 20px; margin-bottom: 20px; border: 1px solid #0ff; animation: fadeIn {delay}s ease-in-out;'>
                    <h3 style='color: #ff00ff; text-shadow: 0 0 5px #ff00ff;'>{blog.get("title", "Untitled")}</h3>
                    <p style='margin: 10px 0;'>{blog.get("description", "No description available.")}</p>
                    <p style='text-align: right; font-size: 12px; color: #0ff;'>
                        {blog.get("date", "Unknown date")}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
            # If no blogs, show an animated empty state
            if not data.get("blogs", []):
                st.markdown("""
                <div style='text-align: center; padding: 40px; border: 1px dashed #ff00ff; border-radius: 10px; animation: borderGlow 4s infinite alternate, fadeIn 1s ease-in-out;'>
                    <p style='color: #ff00ff; font-size: 18px;'>No blog posts available yet. Stay tuned for updates!</p>
                </div>
                """, unsafe_allow_html=True)

        elif choice == "My Resume":
            st.markdown("<h1>MY RESUME</h1>", unsafe_allow_html=True)
            
            # Enhanced resume section
            st.markdown("""
            <div style='animation: fadeIn 1s ease-in-out; text-align: center;'>
                <p style='margin: 20px 0; font-size: 18px;'>
                    Access my complete professional background and skills.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"""
                <div style='text-align: center; padding: 30px; border: 2px solid #0ff; border-radius: 15px; animation: borderGlow 4s infinite alternate, fadeIn 1.5s ease-in-out;'>
                    <a href='{data.get("resume", {}).get("link", "#")}' target='_blank' style='display: block; font-size: 20px; color: #0ff; text-decoration: none;'>
                        <span style='margin-right: 10px; font-size: 24px;'>📄</span>
                        <span style='text-transform: uppercase; letter-spacing: 2px;'>Download Resume</span>
                    </a>
                </div>
                """, unsafe_allow_html=True)
            
            # Skills section with animated bars
            st.markdown("<h3 style='margin-top: 40px;'>SKILLS</h3>", unsafe_allow_html=True)
            
            skills = [
                {"name": "Data Analysis", "level": 90},
                {"name": "Python", "level": 85},
                {"name": "Machine Learning", "level": 75},
                {"name": "SQL", "level": 80},
                {"name": "Data Visualization", "level": 85}
            ]
            
            for i, skill in enumerate(skills):
                st.markdown(f"""
                <div style='margin-bottom: 15px; animation: fadeIn {1 + i*0.2}s ease-in-out;'>
                    <p style='margin-bottom: 5px; display: flex; justify-content: space-between;'>
                        <span>{skill['name']}</span>
                        <span>{skill['level']}%</span>
                    </p>
                    <div style='background: rgba(0,0,0,0.3); border-radius: 10px; height: 10px; position: relative; overflow: hidden;'>
                        <div style='position: absolute; top: 0; left: 0; height: 100%; width: {skill["level"]}%; 
                            background: linear-gradient(90deg, #0ff, #ff00ff); border-radius: 10px;
                            animation: slideIn 2s ease-out, borderGlow 4s infinite alternate;'></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        elif choice == "About Me":
            st.markdown("<h1>ABOUT ME</h1>", unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 2])
            with col1:
                if image:
                    st.image(image, width=250)
                else:
                    # Placeholder avatar with animation if no image is available
                    st.markdown("""
                    <div style='text-align: center; padding: 20px; border: 2px solid #ff00ff; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; animation: borderGlow 4s infinite alternate, fadeIn 2s ease-in-out;'>
                        <svg width="150" height="150" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                            <circle cx="50" cy="35" r="20" fill="none" stroke="#0ff" stroke-width="2" />
                            <path d="M30,70 Q50,90 70,70" fill="none" stroke="#0ff" stroke-width="2" />
                        </svg>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style='animation: fadeIn 1.5s ease-in-out;'>
                    <p style='font-size: 18px; margin-bottom: 20px;'>
                        Hello, I'm <span style='color: #ff00ff; font-weight: bold;'>Ashish</span>, a futuristic data analytics professional...
                    </p>
                    <p>
                        I blend technology with creativity to solve complex data challenges. My journey in the tech world has equipped me with a unique set of skills that allows me to decode patterns and extract meaningful insights from data.
                    </p>
                    <p>
                        When I'm not immersed in data, you can find me exploring new technologies, contributing to open-source projects, or writing about tech trends.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
            # Timeline section
            st.markdown("<h3 style='margin-top: 40px;'>MY JOURNEY</h3>", unsafe_allow_html=True)
            
            timeline_events = [
                {"year": "2024", "event": "Started career in Data Analysis"},
                {"year": "2024", "event": "Completed Advanced Python Certification"},
                {"year": "2025", "event": "Led first major data project"},
                {"year": "2025", "event": "Expanded skills to include Machine Learning"}
            ]
            
            st.markdown("""
            <div style='position: relative; padding-left: 50px; margin-left: 20px; border-left: 2px solid #0ff; animation: borderGlow 4s infinite alternate;'>
            """, unsafe_allow_html=True)
            
            for i, event in enumerate(timeline_events):
                st.markdown(f"""
                <div style='position: relative; margin-bottom: 30px; animation: fadeIn {1 + i*0.3}s ease-in-out;'>
                    <div style='position: absolute; left: -68px; width: 35px; height: 35px; background: linear-gradient(135deg, #0ff, #ff00ff); border-radius: 50%; display: flex; justify-content: center; align-items: center; color: #000; font-weight: bold; box-shadow: 0 0 10px #ff00ff;'>
                        {event["year"]}
                    </div>
                    <p style='margin: 0; padding: 5px 0;'>{event["event"]}</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

        elif choice == "Contact Me":
            st.markdown("<h1>CONTACT ME</h1>", unsafe_allow_html=True)
            
            # Introduction text with animation
            st.markdown("""
            <p style='text-align: center; margin-bottom: 30px; animation: fadeIn 1s ease-in-out;'>
                Have a project in mind or want to collaborate? Reach out through the form below.
            </p>
            """, unsafe_allow_html=True)
            
            # Contact form with enhanced styling
            with st.form("contact_form"):
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("Your Name", placeholder="Enter your full name")
                with col2:
                    email = st.text_input("Your Email", placeholder="Enter your email address")
                
                subject = st.text_input("Subject", placeholder="Enter the subject of your message")
                message = st.text_area("Your Message", placeholder="Write your message here", height=200)
                
                # Animated submit button
                submit_col1, submit_col2, submit_col3 = st.columns([1, 2, 1])
                with submit_col2:
                    submit_button = st.form_submit_button("Send Message")
                
                if submit_button:
                    if name and email and subject and message:
                        st.success(f"Thanks {name}, I'll get back to you soon!")
                        
                        # Add animated success message
                        st.markdown("""
                        <div style='text-align: center; margin-top: 20px; animation: fadeIn 1s ease-in-out;'>
                            <p style='color: #0f0; font-size: 18px;'>Your message has been sent successfully!</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Please fill all fields.")
                        
                        # Add animated error message
                        st.markdown("""
                        <div style='text-align: center; margin-top: 20px; animation: fadeIn 1s ease-in-out;'>
                            <p style='color: #f00; font-size: 18px;'>All fields are required!</p>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Contact information section
            st.markdown("""
            <div style='margin-top: 40px; padding: 20px; border: 1px solid #0ff; border-radius: 10px; background: rgba(0,0,0,0.3); animation: fadeIn 2s ease-in-out, borderGlow 4s infinite alternate;'>
                <h3 style='text-align: center; margin-bottom: 20px;'>ALTERNATIVE CONTACT METHODS</h3>
                <div style='display: flex; justify-content: space-around; text-align: center; flex-wrap: wrap;'>
                    <div style='margin: 10px 20px;'>
                        <p style='font-size: 24px; margin-bottom: 5px;'>📧</p>
                        <p style='color: #ff00ff;'>ak7103300@gmail.com</p>
                    </div>
                    <div style='margin: 10px 20px;'>
                        <p style='font-size: 24px; margin-bottom: 5px;'>📱</p>
                        <p style='color: #ff00ff;'>7078731188</p>
                    </div>
                    <div style='margin: 10px 20px;'>
                        <p style='font-size: 24px; margin-bottom: 5px;'>🔗</p>
                        <p style='color: #ff00ff;'>https://www.linkedin.com/in/ashish-kumar-b5722224b/</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Enhanced Footer with Animated Text
    st.markdown(
        """
        <footer style='text-align: center; padding: 20px; margin-top: 50px; background: linear-gradient(0deg, #0c0c16, transparent); animation: fadeIn 2s ease-in-out;'>
            <p style='font-size: 18px; margin-bottom: 10px; animation: flicker 2s infinite alternate;'>
                <span style='color: #ff00ff;'>[ </span>
                ASHISH'S  PORTFOLIO
                <span style='color: #ff00ff;'> ]</span>
            </p>
            <p style='font-size: 14px; color: #0ff; animation: fadeIn 3s ease-in-out;'>
                © 2024 | Made by Ashish 
            </p>
        </footer>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
