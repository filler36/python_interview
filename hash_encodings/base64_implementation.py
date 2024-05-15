class Base64Util:
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    @classmethod
    def encode(cls, input_str: str) -> str:
        """
        Encode string to base64 encoded string
        """
        bytes_str = bytes(input_str, encoding='utf-8')  # 'hi' -> b'hi'
        bytes_list = [bin(byte) for byte in bytes_str]  # ['0b1101000', '0b1101001']
        binary_str = cls._convert_to_binary_str(bytes_list)  # '0110100001101001'
        six_bit_elements_list = cls._convert_to_six_bit_elements_list(binary_str, 6)  # ['011010', '000110', '100100']
        return cls._encode(six_bit_elements_list)

    @staticmethod
    def _convert_to_binary_str(bytes_list: list) -> str:
        """
        Convert list of bytes to binary string
        For example: ['0b1101000', '0b1101001'] -> '0110100001101001'
        """
        binary_str = ''
        for i in bytes_list:
            bin_symbol = (i[2:].rjust(8, '0'))
            binary_str += bin_symbol
        return binary_str

    @staticmethod
    def _convert_to_six_bit_elements_list(binary_str: str, length: int) -> list:
        """
        Convert binary string to list of 6 bit elements
        For example: '0110100001101001' -> ['011010', '000110', '100100']
        """
        return [binary_str[i:i + length].ljust(6, '0') for i in range(0, len(binary_str), length)]

    @classmethod
    def _encode(cls, six_bit_elements_list: list) -> str:
        """
        Encode list of six bit elements to base64 string
        """
        result = ''
        for i in six_bit_elements_list:
            result += cls.CHARS[int(i, base=2)]
        x = 4 - len(result) % 4
        return result + x * '='


if __name__ == '__main__':
    base64_util = Base64Util()
    print(base64_util.encode('hello'))
