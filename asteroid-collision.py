class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # This will store asteroids that are still moving safely
        for asteroid in asteroids:
            # Check for a collision:
            # Collision only happens if:
            # 1) There is something in the stack
            # 2) Current asteroid is moving left (negative)
            # 3) Top of stack is moving right (positive)
            while stack and asteroid < 0 and stack[-1] > 0:
                # If the top asteroid is smaller, it explodes
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue  # Keep checking for more possible collisions
                # If both are equal size, both explode
                elif stack[-1] == -asteroid:
                    stack.pop()
                # In both equal or larger-top cases, stop checking
                break            
            else:
                # This else runs only if the while loop did NOT break
                # Meaning the asteroid survived all collisions
                stack.append(asteroid)
        return stack  # Remaining asteroids after all collisions
