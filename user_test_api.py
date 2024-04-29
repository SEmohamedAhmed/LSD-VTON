# from gradio_client import Client
#
# client = Client("https://ootd.ibot.cn/", ssl_verify=False)
# result = client.predict(
#     r"C:\Users\Mr.MohamedAhmed\Desktop\IMG_20210306_012228.jpg",
#     # filepath  in 'Model' Image component
#     r"D:\Mohamed\FCIS\4th\GP\VITON\Dataset\VITON-HD[DO NOT EDIT]\test\cloth\00008_00.png",
#     # filepath  in 'Garment' Image component
#     1,  # float (numeric value between 1 and 6) in 'Images' Slider component
#     30,  # float (numeric value between 20 and 40) in 'Steps' Slider component
#     1,  # float (numeric value between 1.0 and 5.0) in 'Guidance scale' Slider component
#     -1,  # float (numeric value between -1 and 2147483647) in 'Seed' Slider component
#     api_name="/process_hd"
# )
# print(result)


###############

# Step 1: Open the original file
with open(r"C:\Users\Mr.MohamedAhmed\Desktop\test_pairs.txt", 'r') as original_file:
    # Step 2: Open a new file for writing
    with open(r"C:\Users\Mr.MohamedAhmed\Desktop\test_pairskoky.txt", 'w') as modified_file:
        # Step 3: Read and modify each line
        for line in original_file:
            # Replace '.jpg' with '.png' and append 'upper'
            modified_line = line.replace('.jpg', '.png')[:-1] + ' upper\n'
            # Step 4: Write the modified line to the new file
            modified_file.write(modified_line)
            # Step 5: Close both files (not necessary here as 'with' statement handles it)
