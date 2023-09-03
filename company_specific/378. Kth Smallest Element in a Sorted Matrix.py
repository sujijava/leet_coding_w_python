class Solution:
    def kthSmallest(self, matrix, k):
        # Get the number of rows and columns of the matrix.
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Define a helper function to count the number of elements in the matrix that are less than or equal to x.
        def count_less_or_equal(target_value):
            count = 0
            col_index = num_cols - 1  # Start with the rightmost column.

            for row_index in range(num_rows):
                # Decrease column index until the current element (located at matrix[row_index][col_index]) is less than or equal to target_value.
                while col_index >= 0 and matrix[row_index][col_index] > target_value:
                    col_index -= 1

                # Update count by adding the number of elements in the current row that are less than or equal to target_value.
                count += (col_index + 1)
            return count

        # Initialize the binary search boundaries with the smallest and largest values in the matrix.
        left_bound, right_bound = matrix[0][0], matrix[-1][-1]
        result = -1

        # Binary search loop.
        while left_bound <= right_bound:
            mid_value = (left_bound + right_bound) // 2

            # If there are at least k elements less than or equal to mid_value,
            # we might have found our answer, but we continue the search on the left side to find the smallest possible value.
            if count_less_or_equal(mid_value) >= k:
                result = mid_value
                # Try looking for a smaller value on the left side.
                right_bound = mid_value - 1
            else:
                # If there are fewer than k elements less than or equal to mid_value,
                # we need to look for a larger value on the right side.
                left_bound = mid_value + 1

        return result
