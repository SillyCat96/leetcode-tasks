"""
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent 
their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, 
both will explode. Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 
"""
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            # Пока стек не пуст и происходит столкновение...
            while stack and asteroid < 0 and stack[-1] > 0:
                # Если текущий астероид больше, взрываем астероид в стеке
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                # Если они равны, взрываем оба
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    break # Текущий астероид тоже взорвался, выходим из цикла
                # Если текущий астероид меньше, он взрывается сам
                else: # abs(asteroid) < stack[-1]
                    break
            # Если цикл завершился без столкновения или текущий астероид выжил...
            else:
                stack.append(asteroid)
                
        return stack

solver = Solution()
print(solver.asteroidCollision([-5,10,5]))