# -*- coding: utf-8 -*-
"""
Streamlit Web Application Entrypoint for General_Graph_Analyzer.html
- GitHub Repository에 업로드하여 Streamlit Community Cloud에 바로 게시할 수 있는 메인 스크립트입니다.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components


def main():
    st.set_page_config(
        page_title="엑셀/CSV 데이터 Graph Analyzer V1.0",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Streamlit 기본 여백 및 헤더/푸터 최소화 스타일 적용 (전체 화면 활용)
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 0.5rem !important;
                padding-bottom: 0rem !important;
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
                max-width: 100% !important;
            }
            header[data-testid="stHeader"] {
                height: 1.5rem;
            }
            footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    html_path = Path(__file__).resolve().parent / "General_Graph_Analyzer.html"

    if not html_path.exists():
        st.error(f"필수 파일 '{html_path.name}'을(를) 찾을 수 없습니다. 같은 폴더에 위치시켜 주세요.")
        return

    html_content = html_path.read_text(encoding="utf-8")

    # General_Graph_Analyzer.html 전체 UI 렌더링
    components.html(html_content, height=940, scrolling=False)


if __name__ == "__main__":
    main()
