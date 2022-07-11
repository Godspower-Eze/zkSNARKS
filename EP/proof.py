from typing import List

from utils import factorizer


class Verifier:

    def __init__(self, degree: int, mod: int, secret: int, base_number: int, coefs_of_t_of_x: List):
        if degree < 1:
            raise Exception("Degree cannot be less than 1")
        if len(coefs_of_t_of_x) != degree:
            raise Exception("t of x has invalid length")
        self.degree = degree
        self.mod = mod
        self.secret = secret
        self.base_number = base_number
        self.coefs_of_t_of_x = coefs_of_t_of_x

    def t_of_x(self) -> int:
        result = 0
        exponent = len(self.coefs_of_t_of_x) - 1
        for i in self.coefs_of_t_of_x:
            result += i * (self.secret ** exponent)
            exponent -= 1
        print(result)
        return result

    def encrypt(self) -> List:
        encrypted_values = []
        for i in range(self.degree):
            encrypted_value = (self.base_number ** (self.secret ** i)) % self.mod
            encrypted_values.append(encrypted_value)
        print(encrypted_values)
        return encrypted_values[::-1]


# verifier_instance = Verifier(3, 5, 23, 17, [1, -3, 2])
# verifier_instance.t_of_x()
# verifier_instance.encrypt()


class Prover:

    def __init__(self, degree: int, mod: int, coefs_of_t_of_x: List, coefs_of_p_of_x: List, encrypted_values: List):
        if len(coefs_of_p_of_x) != degree or len(encrypted_values) != degree:
            raise Exception(
                "`degree` should be equal to length of encrypted values and length of co-efficients of p of x")
        self.degree = degree
        self.mod = mod
        self.coefs_of_t_of_x = coefs_of_t_of_x
        self.coefs_of_p_of_x = coefs_of_p_of_x
        self.encrypted_values = encrypted_values

    def h_of_x(self):
        quo_and_rem, rem_is_zero = factorizer(self.coefs_of_p_of_x, self.coefs_of_t_of_x)
        if not rem_is_zero:
            raise Exception("h(x) has a remainder")
        return quo_and_rem[0]

    def compute_p_of_x_with_encryped_values(self) -> int:
        encryped_values_exponent_coefs = [i[0] ** i[1] for i in zip(self.encrypted_values,
                                                                    self.coefs_of_p_of_x)]  # Encrypted values with
        multiple = 1
        for i in encryped_values_exponent_coefs:
            multiple *= i
        return multiple % self.mod

    def compute_h_of_x_with_encryped_values(self, h_of_x: List) -> List:
        length = len(h_of_x)
        print(h_of_x)
        print(self.encrypted_values)
        needed_encrypted_values = [i for i in self.encrypted_values if self.encrypted_values.index(i) <= length - 1]
        print(needed_encrypted_values)
        # return needed_encrypted_values


# prover_instance = Prover(3, 5, [2], [4, 1, 2], [1, 3, 4])
# prover_instance.compute_h_of_x_with_encryped_values([1, 2])
