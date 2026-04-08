# # 演示 continue 和 break 在 for 循环中的使用
# print("=== for 循环中的 continue 和 break ===")
# for i in range(1, 6):
#     if i == 3:
#         print(f"遇到 i={i}，执行 continue，跳过本次循环")
#         continue
#     if i == 5:
#         print(f"遇到 i={i}，执行 break，终止循环")
#         break
#     print(f"当前 i={i}")


# # 演示 continue 和 break 在 while 循环中的使用
# print("\n=== while 循环中的 continue 和 break ===")
# j = 1
# while j <= 5:
#     if j == 3:
#         print(f"遇到 j={j}，执行 continue，跳过本次循环")
#         j += 1
#         continue
#     if j == 5:
#         print(f"遇到 j={j}，执行 break，终止循环")
#         break
#     print(f"当前 j={j}")
#     j += 1


# # 演示 continue 和 break 在嵌套循环中的使用
# print("\n=== 嵌套循环中的 continue 和 break ===")
# for i in range(1, 4):
#     print(f"\n外层循环 i={i}")
#     for j in range(1, 4):
#         if j == 2:
#             print(f"  内层循环 j={j}，执行 continue，跳过本次内层循环")
#             continue
#         if j == 3:
#             print(f"  内层循环 j={j}，执行 break，终止内层循环")
#             break
#         print(f"  当前 j={j}")
