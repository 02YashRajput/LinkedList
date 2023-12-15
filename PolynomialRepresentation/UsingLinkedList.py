class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


class PolynomialLinkedList:
    def __init__(self):
        self.head = None

    def insert_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if (not self.head) or (exponent > self.head.exponent):
            # Insert at the beginning if the list is empty or the new term has the highest exponent
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and exponent < current.next.exponent:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def add_polynomials(self, poly2):
        result = PolynomialLinkedList()
        current1, current2 = self.head, poly2.head

        while current1 or current2:
            if not current2 or (current1 and current1.exponent > current2.exponent):
                result.insert_term(current1.coefficient, current1.exponent)
                current1 = current1.next
            elif not current1 or (current2 and current2.exponent > current1.exponent):
                result.insert_term(current2.coefficient, current2.exponent)
                current2 = current2.next
            else:
                # Exponents are equal, add coefficients
                result.insert_term(current1.coefficient + current2.coefficient, current1.exponent)
                current1 = current1.next
                current2 = current2.next

        return result

    def subtract_polynomials(self, poly2):
        result = PolynomialLinkedList()
        current1, current2 = self.head, poly2.head

        while current1 or current2:
            if not current2 or (current1 and current1.exponent > current2.exponent):
                result.insert_term(current1.coefficient, current1.exponent)
                current1 = current1.next
            elif not current1 or (current2 and current2.exponent > current1.exponent):
                result.insert_term(-current2.coefficient, current2.exponent)
                current2 = current2.next
            else:
                # Exponents are equal, subtract coefficients
                result.insert_term(current1.coefficient - current2.coefficient, current1.exponent)
                current1 = current1.next
                current2 = current2.next

        return result

    def delete_term(self, exponent):
        if not self.head:
            print("Empty Polynomial")
            return

        if self.head.exponent == exponent:
            # Delete the first node if it matches the given exponent
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.exponent != exponent:
                current = current.next
            if current.next:
                current.next = current.next.next
            else:
                print(f"Term with exponent {exponent} not found")

    def print_polynomial(self):
        if not self.head:
            print("Empty Polynomial")
            return

        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            current = current.next
            if current:
                print("+", end=" ")
        print()


# Example usage
poly1 = PolynomialLinkedList()
poly1.insert_term(3, 2)
poly1.insert_term(4, 1)
poly1.insert_term(2, 0)

poly2 = PolynomialLinkedList()
poly2.insert_term(1, 3)
poly2.insert_term(2, 1)
poly2.insert_term(5, 0)

print("Polynomial 1:")
poly1.print_polynomial()

print("Polynomial 2:")
poly2.print_polynomial()

print("Addition Result:")
result_addition = poly1.add_polynomials(poly2)
result_addition.print_polynomial()

print("Subtraction Result:")
result_subtraction = poly1.subtract_polynomials(poly2)
result_subtraction.print_polynomial()

print("After Deleting Term with Exponent 1 from Polynomial 1:")
poly1.delete_term(1)
poly1.print_polynomial()
