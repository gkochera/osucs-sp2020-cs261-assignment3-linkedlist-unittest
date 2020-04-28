import unittest
from linked_list import CircularList, LinkedList

#FixMe: Check contains after remove for both types of lists and all remove functions (edge cases in particular!)

class LinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList()

    def fill_linked_list_with_data(self):
        self.ll = LinkedList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_add_link_before_empty_list(self):
        self.ll.add_link_before("A", 0)
        self.assertEqual(self.ll.get_front(), "A")

    def test_add_link_before(self):
        self.ll.add_link_before("A", 0)
        self.ll.add_link_before("B", 1)
        self.ll.add_link_before("C", 2)
        self.assertEqual(self.ll.get_front(), "A")
        self.assertEqual(self.ll.get_back(), "C")

    def test_add_link_before_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.ll.add_link_before('Z', 26)

    def test_add_link_before_negative_index(self):
        with self.assertRaises(IndexError):
            self.ll.add_link_before("@", -2)

    def test_add_link_before_multiple_times_same_index_empty_list(self):
        self.ll.add_link_before("H", 0)
        self.ll.add_link_before("G", 0)
        self.ll.add_link_before("F", 0)
        self.assertEqual(self.ll.__str__(), '[F -> G -> H]')

    def test_remove_link_empty_list(self):
        with self.assertRaises(IndexError):
            self.ll.remove_link(1)

    def test_remove_link_negative_index(self):
        with self.assertRaises(IndexError):
            self.ll.remove_link(-93)

    def test_remove_link(self):
        self.ll.add_back("A")
        self.ll.add_back("B")
        self.ll.add_back("C")
        self.ll.remove_link(1)
        self.assertEqual("A", self.ll.get_front())
        self.assertEqual("C", self.ll.get_back())
        self.assertFalse(self.ll.contains("B"))

    def test_add_front(self):
        self.ll.add_front("A")
        self.ll.add_front("B")
        self.ll.add_front("C")
        self.assertEqual(self.ll.get_front(), "C")

    def test_add_back(self):
        self.ll.add_back("X")
        self.ll.add_back("Y")
        self.ll.add_back("Z")
        self.assertEqual("Z", self.ll.get_back())

    def test_get_front(self):
        self.fill_linked_list_with_data()
        self.assertEqual(self.ll.get_front(), "A")
        self.assertEqual(self.ll.get_front(), "A")

    def test_get_back(self):
        self.fill_linked_list_with_data()
        self.assertEqual(self.ll.get_back(), "G")
        self.assertEqual(self.ll.get_back(), "G")

    def test_remove_front(self):
        self.fill_linked_list_with_data()
        self.ll.remove_front()
        self.assertEqual(self.ll.get_front(), "B")

    def test_remove_back(self):
        self.fill_linked_list_with_data()
        self.ll.remove_back()
        self.assertEqual(self.ll.get_back(), "F")

    def test_is_empty_on_non_empty_list(self):
        self.fill_linked_list_with_data()
        self.assertFalse(self.ll.is_empty())

    def test_is_empty_on_empty_list(self):
        self.assertTrue(self.ll.is_empty())

    def test_contains_value_not_in_list(self):
        self.fill_linked_list_with_data()
        self.assertFalse(self.ll.contains("X"))

    def test_contains_value_in_list(self):
        self.fill_linked_list_with_data()
        self.assertTrue(self.ll.contains("C"))

    def test_contains_duplicate_values_in_list(self):
        self.fill_linked_list_with_data()
        self.ll.add_back("A")
        self.assertTrue(self.ll.contains("A"))

    def test_contains_after_remove_first_item(self):
        self.fill_linked_list_with_data()
        self.ll.remove('A')
        self.assertFalse(self.ll.contains('A'))

    def test_contains_after_remove_last_item(self):
        self.fill_linked_list_with_data()
        self.ll.remove('G')
        self.assertFalse(self.ll.contains('G'))

    def test_remove_empty_list(self):
        self.ll.remove("Z")
        self.assertEqual(self.ll.get_front(), None)

    def test_remove_value_in_list(self):
        self.fill_linked_list_with_data()
        self.ll.remove("D")
        for i in range(3):
            self.ll.remove_front()
        self.assertEqual(self.ll.get_front(), "E")

    def test_remove_value_not_in_list(self):
        self.fill_linked_list_with_data()
        self.ll.remove('X')
        self.assertEqual(self.ll.__str__(), '[A -> B -> C -> D -> E -> F -> G]')


class CircularListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cl = CircularList()

    def fill_circular_list_with_data(self):
        self.cl = CircularList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_add_link_before_empty_list(self):
        self.cl.add_link_before("A", 0)
        self.assertEqual(self.cl.get_front(), "A")

    def test_add_link_before_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_link_before('X', 3)
        for i in range(3):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'X')

    def test_add_link_before_out_of_bounds_index(self):
        self.fill_circular_list_with_data()
        self.cl.add_link_before('X', 100)
        for i in range(4):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'X')

    def test_remove_link_empty_list(self):
        with self.assertRaises(IndexError):
            self.cl.remove_link(3)

    def test_remove_link_negative_index(self):
        with self.assertRaises(IndexError):
            self.cl.remove_link(-9)

    def test_remove_link_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove_link(3)
        for i in range(3):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'E')

    def test_add_front_empty_list(self):
        self.cl.add_front('X')
        self.assertEqual(self.cl.get_front(), 'X')

    def test_add_front_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_front('X')
        self.assertEqual(self.cl.get_front(), 'X')

    def test_add_back_empty_list(self):
        self.cl.add_back('X')
        self.assertEqual(self.cl.get_back(), 'X')

    def test_add_back_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_back('X')
        self.assertEqual(self.cl.get_back(), 'X')

    def test_get_front_empty_list(self):
        self.assertEqual(self.cl.get_front(), None)

    def test_get_front_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.assertEqual(self.cl.get_front(), 'A')

    def test_get_back_empty_list(self):
        self.assertEqual(self.cl.get_back(), None)

    def test_get_back_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.assertEqual(self.cl.get_back(), 'G')

    def test_remove_front_empty_list(self):
        self.cl.remove_front()
        self.assertEqual(self.cl.sentinel.next, self.cl.sentinel)

    def test_remove_front_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'B')

    def test_remove_back_empty_list(self):
        self.cl.remove_back()
        self.assertEqual(self.cl.sentinel.next, self.cl.sentinel)

    def test_remove_back_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove_back()
        self.assertEqual(self.cl.get_back(), 'F')

    def test_is_empty_empty_list(self):
        self.assertTrue(self.cl.is_empty())

    def test_is_empty_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.assertFalse(self.cl.is_empty())

    def test_contains_empty_list(self):
        self.assertFalse(self.cl.contains(''))

    def test_contains_non_empty_list_value_in_list(self):
        self.fill_circular_list_with_data()
        self.assertTrue(self.cl.contains('D'))

    def test_contains_non_empty_list_value_duplicate_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_front('E')
        self.assertTrue(self.cl.contains('E'))

    def test_contains_non_empty_list_value_not_in_list(self):
        self.fill_circular_list_with_data()
        self.assertFalse(self.cl.contains('X'))

    def test_remove_value_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove('C')
        for i in range(2):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'D')

    def test_remove_value_not_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove('X')
        self.assertEqual(self.cl.__str__(), '[A <-> B <-> C <-> D <-> E <-> F <-> G]')

    def test_remove_duplicate_value_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_front('G')
        self.cl.remove('G')
        self.assertEqual(self.cl.__str__(), '[A <-> B <-> C <-> D <-> E <-> F <-> G]')

    def test_circular_list_reverse_empty_list(self):
        self.cl.circularListReverse()
        self.assertEqual(self.cl.sentinel.next, self.cl.sentinel)

    def test_circular_list_reverse_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.circularListReverse()
        self.assertEqual(self.cl.__str__(), '[G <-> F <-> E <-> D <-> C <-> B <-> A]')


if __name__ == '__main__':
    unittest.main()
