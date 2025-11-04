def count_bitonic_sequences(N):
    MOD = 10 ** 9 + 7
    memo = {}

    def dp(sum_left, last_value, phase):
        # Base case: no sum remaining
        if sum_left == 0:
            return 1

        # Check memo
        if (sum_left, last_value, phase) in memo:
            return memo[(sum_left, last_value, phase)]

        count = 0

        if phase == 0:  # Increasing phase
            # Option 1: Stay in increasing phase - place next_val >= last_value
            for next_val in range(last_value, sum_left + 1):
                count += dp(sum_left - next_val, next_val, 0)
                count %= MOD

            # Option 2: Switch to decreasing phase - place next_val < last_value (STRICTLY LESS!)
            for next_val in range(1, min(last_value, sum_left + 1)):
                count += dp(sum_left - next_val, next_val, 1)
                count %= MOD

        else:  # phase == 1 (Decreasing phase)
            # Must stay decreasing - place next_val <= last_value
            for next_val in range(1, min(last_value + 1, sum_left + 1)):
                count += dp(sum_left - next_val, next_val, 1)
                count %= MOD

        memo[(sum_left, last_value, phase)] = count
        return count

    # Start by placing the first value (from 1 to N)
    total = 0
    for first_val in range(1, N + 1):
        total += dp(N - first_val, first_val, 0)
        total %= MOD

    return total

print(count_bitonic_sequences(10))

# Test
# for N in range(1, 6):
