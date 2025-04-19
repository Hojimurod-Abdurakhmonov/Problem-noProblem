# Today I start solve problee in leetcode


#If-else

# number  = int(input("Enter age: "))
# if number<18:
#     print("Don't accsess")
# else:
#     print("Welcome bar")

# hot = float(input("Enter your body temperature (°C): "))
#
# if hot < 36.0:
#     print("⚠️ Warning: Your body temperature is too low. Seek medical attention.")
# elif 36.0 <= hot <= 36.8:
#     print("✅ Your body temperature is normal.")
# else:
#     print("🚑 High temperature detected. Please visit a hospital.")


# def removeDuplicates(self, nums: List[int]) -> int:
#     if not nums:  # Agar ro'yxat bo'sh bo'lsa, 0 qaytariladi
#         return 0
#
#     a = 0  # a - bu unikal elementlar joylashadigan indeks
#
#     for b in range(1, len(nums)):  # b - hozirgi qaralayotgan element
#         if nums[b] != nums[a]:  # Agar yangi unikal son topilsa
#             a += 1  # a ni keyingi bo'sh joyga siljitamiz
#             nums[a] = nums[b]  # yangi unikal sonni joylashtiramiz
#
#     return a + 1

#This is very hard for every beginner