import qrcode

class QRManager:
    def generate_qr(self, student_id):
        img = qrcode.make(student_id)
        img.save(f"{student_id}_qr.png")
        print("QR code generated successfully!")