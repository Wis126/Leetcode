class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Chuyển số nguyên thành chuỗi để dễ xử lý từng chữ số
        digits = [int(digit) for digit in str(n)]

        # Tính tích và tổng của các chữ số
        product = 1
        summation = 0
        for digit in digits:
            product *= digit
            summation += digit

        # Trả về hiệu giữa tích và tổng
        return product - summation