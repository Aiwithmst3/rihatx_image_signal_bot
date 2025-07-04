from 4_signal_reporter import generate_report

...

    st.success("✅ Signal Generated")
    st.markdown(f"### 📈 Signal: `{result['signal']}`")
    st.markdown(f"🧠 Confidence: `{result['confidence']}%`")
    st.markdown(f"📝 Strategy Match: `{result['detected_info']}`")

    if st.button("📥 Export Report as CSV"):
        df = generate_report(result['signal'], result['confidence'], result['detected_info'].split(", "))
        st.download_button("Download CSV", df.to_csv(index=False), "signal_report.csv", "text/csv")
