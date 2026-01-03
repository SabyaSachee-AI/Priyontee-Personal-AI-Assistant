from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from xml.sax.saxutils import escape  # <-- for escaping special characters

class PDFExporter:
    def export(self, history, filename="priyontee_chat.pdf"):
        doc = SimpleDocTemplate(filename, pagesize=A4)
        styles = getSampleStyleSheet()
        content = []

        # Title
        content.append(
            Paragraph("<b>Priyontee! – AI Assistant Chat History</b>", styles["Title"])
        )
        content.append(Spacer(1, 12))

        # Chat history
        for chat in history:
            # Escape any HTML special characters in the message
            safe_message = escape(chat['message'])
            content.append(
                Paragraph(f"<b>{chat['role']}:</b> {safe_message}", styles["Normal"])
            )
            content.append(Spacer(1, 8))

        doc.build(content)
        return filename
