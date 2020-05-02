import unittest
from linked_list import CircularList, LinkedList

# Type your exception message below.
YOUR_EXCEPTION_MESSAGE = "Index out of bounds"

class LinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList()

    # Creates a new linked list with the letters A through G inclusive. 7 elements total. Referred to as 'standard
    # fill' in comments.
    def fill_linked_list_with_data(self):
        self.ll = LinkedList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    # Inserts the letter 'A' at index 0 in an empty list, checks to see if it is at the front of the list.
    def test_add_link_before_empty_list(self):
        self.ll.add_link_before("A", 0)
        self.assertEqual(self.ll.__str__(), '[A]')

    # Inserts A at index 0, B at index 1 and C at index 2. Asserts A is at the front and C is at the back.
    # test_add_link_before: Changed indexes to match assignment 3 guidelines example, does not allow for creating a
    # new node past the list's length
    def test_add_link_before(self):
        self.ll.add_link_before("A", 0)
        self.ll.add_link_before("B", 0)
        self.ll.add_link_before("C", 1)
        self.assertEqual(self.ll.__str__(), '[B -> C -> A]')

    def test_add_link_before_out_of_bounds_index_n(self):
        self.ll.add_link_before("A", 0)
        self.ll.add_link_before("B", 0)
        self.ll.add_link_before("C", 1)

        try:
            with self.assertRaises(IndexError):
                self.ll.add_link_before("D", 3)
        except Exception as msg:
             self.assertEqual(msg.args[0], YOUR_EXCEPTION_MESSAGE)
            
    # Tries to insert Z at index 26 in an empty list, verifies an IndexError is raised.
    def test_add_link_before_out_of_bounds(self):
        try:
            with self.assertRaises(IndexError):
                self.ll.add_link_before('Z', 26)
        except Exception as msg:
            self.assertEqual(msg.args[0], YOUR_EXCEPTION_MESSAGE)
          
    # Tries to insert the '@' symbol at index -2, verifies an IndexError is raised.
    def test_add_link_before_negative_index(self):
        try:
            with self.assertRaises(IndexError):
                self.ll.add_link_before("@", -2)
        except Exception as msg:
            self.assertEqual(msg.args[0], YOUR_EXCEPTION_MESSAGE)

    # Inserts H, G and F at index 0. Verifies F is before G and G is before H.
    def test_add_link_before_multiple_times_same_index_empty_list(self):
        self.ll.add_link_before("H", 0)
        self.ll.add_link_before("G", 0)
        self.ll.add_link_before("F", 0)
        self.assertEqual(self.ll.__str__(), '[F -> G -> H]')
  
    def test_add_link_before_fails_at_link_before_tail(self):
        self.ll.add_front('B')
        self.ll.add_front('A')
        with self.assertRaises(IndexError):
            self.ll.add_link_before('C', 2)

    # Tries to remove a link in an empty list, verifies an IndexError is raised.
    def test_remove_link_empty_list(self):
        with self.assertRaises(IndexError):
            self.ll.remove_link(1)

    # Tries to remove a link at a negative index, verifies an IndexError is raised.
    def test_remove_link_negative_index(self):
        with self.assertRaises(IndexError):
            self.ll.remove_link(-93)

    # Adds A, B and C to list respectively. Removes B. Verifies A is first, C is last and B is gone.
    def test_remove_link(self):
        self.ll.add_back("A")
        self.ll.add_back("B")
        self.ll.add_back("C")
        self.ll.remove_link(1)
        self.assertEqual("A", self.ll.get_front())
        self.assertEqual("C", self.ll.get_back())
        self.assertFalse(self.ll.contains("B"))

    # Adds A then B and C to front, respectively, verifies that C is at the front.
    def test_add_front(self):
        self.ll.add_front("A")
        self.ll.add_front("B")
        self.ll.add_front("C")
        self.assertEqual(self.ll.get_front(), "C")

    # Adds X, Y then Z to the back. Verifies that Z is at the back.
    def test_add_back(self):
        self.ll.add_back("X")
        self.ll.add_back("Y")
        self.ll.add_back("Z")
        self.assertEqual("Z", self.ll.get_back())

    # Using the standard fill (A through G), verifies that get_front() returns A and doesn't remove it.
    def test_get_front(self):
        self.fill_linked_list_with_data()
        self.assertEqual(self.ll.get_front(), "A")
        self.assertEqual(self.ll.get_front(), "A")

    # Using the standard fill, verifies that get_back() returns G and doesn't remove it.
    def test_get_back(self):
        self.fill_linked_list_with_data()
        self.assertEqual(self.ll.get_back(), "G")
        self.assertEqual(self.ll.get_back(), "G")

    # Using standard fill, removes the front (A) and verifies that B is now the front.
    def test_remove_front(self):
        self.fill_linked_list_with_data()
        self.ll.remove_front()
        self.assertEqual(self.ll.get_front(), "B")

    # Using standard fill, removes back (G) and verifies that F is now the back.
    def test_remove_back(self):
        self.fill_linked_list_with_data()
        self.ll.remove_back()
        self.assertEqual(self.ll.get_back(), "F")

    # Verifies a list with data is not empty.
    def test_is_empty_on_non_empty_list(self):
        self.fill_linked_list_with_data()
        self.assertFalse(self.ll.is_empty())

    # Verifies a list without data is empty.
    def test_is_empty_on_empty_list(self):
        self.assertTrue(self.ll.is_empty())

    # Verifies a list that had data, and is now empty, is empty.
    def test_is_empty_on_empty_list_that_was_previously_populated(self):
        self.fill_linked_list_with_data()
        for i in range(7):
            self.ll.remove_front()
        self.assertTrue(self.ll.is_empty())

    # Verifies a value not in list causes contains() to return False.
    def test_contains_value_not_in_list(self):
        self.fill_linked_list_with_data()
        self.assertFalse(self.ll.contains("X"))

    # Verifies a value in the list causes contains() to return True.
    def test_contains_value_in_list(self):
        self.fill_linked_list_with_data()
        self.assertTrue(self.ll.contains("C"))

    # Verifies that when a value is in the list more than once, contains(value) will still return True.
    def test_contains_duplicate_values_in_list(self):
        self.fill_linked_list_with_data()
        self.ll.add_back("A")
        self.assertTrue(self.ll.contains("A"))

    # Verifies that contains(value) reports False, when the value removed is the first value in the list.
    def test_contains_after_remove_first_item(self):
        self.fill_linked_list_with_data()
        self.ll.remove('A')
        self.assertFalse(self.ll.contains('A'))

    # Verifies that contains(value) reports False, when the value removed is the last value in the list.
    def test_contains_after_remove_last_item(self):
        self.fill_linked_list_with_data()
        self.ll.remove('G')
        self.assertFalse(self.ll.contains('G'))

    # Verifies that contains(value) reports False, when the value removed (by index) is the first value in the list.
    def test_contains_after_remove_link(self):
        self.fill_linked_list_with_data()
        self.ll.remove_link(0)
        self.assertFalse(self.ll.contains('A'))

    # Verifies that contains(value) reports False, when the value removed (by index) is the last value in the list.
    def test_contains_after_remove_link_end_of_list(self):
        self.fill_linked_list_with_data()
        self.ll.remove_link(6)
        self.assertFalse(self.ll.contains('G'))

    # Verify None is returned by get_front() when a value is removed from an empty list.
    def test_remove_empty_list(self):
        self.ll.remove("Z")
        self.assertEqual(self.ll.get_front(), None)

    # Verify when remove(value) works as expected.
    def test_remove_value_in_list(self):
        self.fill_linked_list_with_data()
        self.ll.remove("D")
        for i in range(3):
            self.ll.remove_front()
        self.assertEqual(self.ll.get_front(), "E")

    # Verify a populated list doesn't change when a value is removed which does not exist in the list.
    def test_remove_value_not_in_list(self):
        self.fill_linked_list_with_data()
        self.ll.remove('X')
        self.assertEqual(self.ll.__str__(), '[A -> B -> C -> D -> E -> F -> G]')


class CircularListTest(unittest.TestCase):

    # Create a CircularList
    def setUp(self) -> None:
        self.cl = CircularList()

    # Same standard fill as LinkedList.
    def fill_circular_list_with_data(self):
        self.cl = CircularList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    # Add A to index 0 of an empty list, then verify its in the front.
    def test_add_link_before_empty_list(self):
        self.cl.add_link_before("A", 0)
        self.assertEqual(self.cl.get_front(), "A")

    # Use standard fill, insert X at index 3, then remove 3 elements from the front and verify X is now the front.
    def test_add_link_before_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_link_before('X', 3)
        for i in range(3):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'X')

    # Try to add X at index 100, verify Index Error is raised.
    def test_add_link_before_out_of_bounds_index_empty_list(self):
        with self.assertRaises(IndexError):
            self.cl.add_link_before('X', 100)

    # Use standard fill, try to add X at index 100, verify Index Error is raised.
    def test_add_link_before_out_of_bounds_index_nonempty_list(self):
        self.fill_circular_list_with_data()
        with self.assertRaises(IndexError):
            self.cl.add_link_before('X', 100)

    # Use standard fill, try to add X at index just prior to tail, verify Index Error is raised.
    def test_add_link_before_index_prior_to_tail_fails(self):
        self.fill_circular_list_with_data()
        with self.assertRaises(IndexError):
            self.cl.add_link_before('X', 7)

    # Verify IndexError raised when removing link at index 3 on empty list.
    def test_remove_link_empty_list(self):
        with self.assertRaises(IndexError):
            self.cl.remove_link(3)

    # Verify IndexError is raised when removing link at a negative index.
    def test_remove_link_negative_index(self):
        with self.assertRaises(IndexError):
            self.cl.remove_link(-9)

    # Use standard fill, remove D at index 3, remove the front 3 values, verify E is the front.
    def test_remove_link_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove_link(3)
        for i in range(3):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'E')

    # Add X to front of empty list, make sure its the front.
    def test_add_front_empty_list(self):
        self.cl.add_front('X')
        self.assertEqual(self.cl.get_front(), 'X')

    # Use standard fill, add X to front of the list, verify X is the front of the list.
    def test_add_front_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_front('X')
        self.assertEqual(self.cl.get_front(), 'X')

    # Add X to back of empty list, verify its the back of the list.
    def test_add_back_empty_list(self):
        self.cl.add_back('X')
        self.assertEqual(self.cl.get_back(), 'X')

    # Use standard fill, add X to back of the list, verify X is back of list.
    def test_add_back_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_back('X')
        self.assertEqual(self.cl.get_back(), 'X')

    # Verify get_front() returns None on empty list.
    def test_get_front_empty_list(self):
        self.assertEqual(self.cl.get_front(), None)

    # Verify get_front() returns A for list containing standard fill.
    def test_get_front_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.assertEqual(self.cl.get_front(), 'A')

    # Verify get_front() returns None on list that is now empty, that once had data.
    def test_get_front_empty_list_that_was_previously_populated(self):
        self.fill_circular_list_with_data()
        for i in range(7):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), None)

    # Verify get_back() returns None for an empty list.
    def test_get_back_empty_list(self):
        self.assertEqual(self.cl.get_back(), None)

    # Verify get_back() returns G for a list containing the standard fill.
    def test_get_back_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.assertEqual(self.cl.get_back(), 'G')

    # Verify get_back() returns None on list that is now empty, that once had data.
    def test_get_back_empty_list_that_was_previously_populated(self):
        self.fill_circular_list_with_data()
        for i in range(7):
            self.cl.remove_back()
        self.assertEqual(self.cl.get_back(), None)

    # Verify remove_front() on empty list does nothing and sentinel still exists.
    def test_remove_front_empty_list(self):
        self.cl.remove_front()
        self.assertEqual(self.cl.sentinel.next, self.cl.sentinel)

    # Verify remove_front() on standard filled list causes B to be new front.
    def test_remove_front_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'B')

    # Verify remove_back() on empty list does nothing and sentinel still exists.
    def test_remove_back_empty_list(self):
        self.cl.remove_back()
        self.assertEqual(self.cl.sentinel.next, self.cl.sentinel)

    # Verify remove_back() on standard filled list causes F to be new back of list.
    def test_remove_back_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove_back()
        self.assertEqual(self.cl.get_back(), 'F')

    # Verify is_empty() is True for an empty list.
    def test_is_empty_empty_list(self):
        self.assertTrue(self.cl.is_empty())

    # Verify is_empty() is False for a list with data.
    def test_is_empty_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.assertFalse(self.cl.is_empty())

    # Verify is_empty() is True for an empty list that once had data.
    def test_is_empty_on_empty_list_that_once_had_data(self):
        self.fill_circular_list_with_data()
        for i in range(7):
            self.cl.remove_back()
        self.assertTrue(self.cl.is_empty())

    # Verify contains() returns False on an empty list with an empty string.
    def test_contains_empty_list(self):
        self.assertFalse(self.cl.contains(''))

    # Verify contains() returns True when value is in list.
    def test_contains_non_empty_list_value_in_list(self):
        self.fill_circular_list_with_data()
        self.assertTrue(self.cl.contains('D'))

    # Verify contains() returns True when value is in list more than once.
    def test_contains_non_empty_list_value_duplicate_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_front('E')
        self.assertTrue(self.cl.contains('E'))

    # Verify contains() returns False when value is not in list.
    def test_contains_non_empty_list_value_not_in_list(self):
        self.fill_circular_list_with_data()
        self.assertFalse(self.cl.contains('X'))

    # Verify removing C from standard fill actually removes it.
    def test_remove_value_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove('C')
        for i in range(2):
            self.cl.remove_front()
        self.assertEqual(self.cl.get_front(), 'D')

    # Verify removing a value not in the list does nothing.
    def test_remove_value_not_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.remove('X')
        self.assertEqual(self.cl.__str__(), '[A <-> B <-> C <-> D <-> E <-> F <-> G]')

    # Verify when a duplicate value is in a list, remove() only removes the first instance.
    def test_remove_duplicate_value_in_list(self):
        self.fill_circular_list_with_data()
        self.cl.add_front('G')
        self.cl.remove('G')
        self.assertEqual(self.cl.__str__(), '[A <-> B <-> C <-> D <-> E <-> F <-> G]')

    # Verify reversing an empty CircularList does nothing.
    def test_circular_list_reverse_empty_list(self):
        self.cl.circularListReverse()
        self.assertEqual(self.cl.sentinel.next, self.cl.sentinel)

    # Verify reversing an standard filled CircularList yields the correct result.
    def test_circular_list_reverse_non_empty_list(self):
        self.fill_circular_list_with_data()
        self.cl.circularListReverse()
        self.assertEqual(self.cl.__str__(), '[G <-> F <-> E <-> D <-> C <-> B <-> A]')


if __name__ == '__main__':
    unittest.main()
