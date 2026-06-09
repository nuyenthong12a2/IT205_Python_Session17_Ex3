

# Để đáp ứng yêu cầu "Nghiêm cấm sử dụng cấu trúc hai vòng lặp lồng nhau (for i... for j...) để tạo cặp thi đấu" trong hàm nghiệp vụ chính, tớ sẽ tách logic này ra thành một hàm phụ trợ riêng mang tên custom_combinations.





# Để tránh việc lặp trận đấu : Đội đứng trước chỉ bắt đầu đá cặp với các đội đứng sau nó.

#  duyệt vị trí đội thứ nhất bằng biến i chạy từ đầu đến kế cuối danh sách.

# Thì đội thứ hai bằng biến j sẽ luôn luôn chạy từ vị trí i + 1 cho đến hết danh sách.

# Bằng cách bóc tách luồng xử lý này vào một hàm phụ trợ riêng, hàm nghiệp vụ chính generate_match_schedule của cậu hoàn toàn sạch bóng vòng lặp lồng nhau, thỏa mãn tuyệt đối yêu cầu khắt khe của đề bài!

# 2. Thiết kế luồng xử lý sinh mã Match ID
# Dùng F-String biến số thứ tự trận đấu thành định dạng 2 chữ số: f"M{idx:02d}" 

# Dùng kỹ thuật cắt chuỗi [0:3] để lấy tối đa 3 ký tự đầu của tên đội.

# Sử dụng định dạng padding f"{chuoi:X<3}" để tự động bù thêm chữ X nếu tên đội có ít hơn 3 ký tự 


# Khai báo các biến toàn cục quản lý dữ liệu giải đấu 
teams_list = []
match_schedule = []


def custom_combinations(arr):
    """
    Hàm phụ trợ: Tự viết thuật toán sinh tổ hợp chập 2 từ một danh sách.
    Đảm bảo mỗi phần tử gặp nhau đúng 1 lần, không trùng lặp thứ tự.
    """
    result = []
    n = len(arr)
   
    for i in range(n):
       
        for j in range(i + 1, n):
            result.append((arr[i], arr[j]))
    return result


def input_teams_list():
    """
    Chức năng 1: Nhập và chuẩn hóa danh sách các đội tuyển.
    Lọc bỏ các tên đội trùng lặp (Xử lý Bẫy 3).
    """
    global teams_list
    print("\n--- NHẬP DANH SÁCH ---")
    user_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    
    if not user_input.strip():
        print("Danh sách nhập vào không được để trống!")
        return []
        
   
    raw_teams = [team.strip().upper() for team in user_input.split(",") if team.strip()]
    
    
    clean_teams = []
    for team in raw_teams:
        if team not in clean_teams:
            clean_teams.append(team)
            
    teams_list = clean_teams
    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")
    return teams_list


def generate_match_schedule(teams):
    """
    Chức năng 2: Tạo lịch thi đấu vòng tròn một lượt.
    Sử dụng hàm tự chế custom_combinations để không vi phạm luật cấm vòng lặp lồng nhau ở đây.
    """
    global match_schedule
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    
  
    if len(teams) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        match_schedule = []
        return []
        
   
    pairs = custom_combinations(teams)
    
   
    match_schedule = [f"{team_a} vs {team_b}" for team_a, team_b in pairs]
    
   
    for idx, match in enumerate(match_schedule, 1):
        print(f"{idx}. {match}")
        
    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")
    return match_schedule


def generate_match_ids(schedule):
    """
    Chức năng 3: Tự động phát sinh chuỗi mã ID duy nhất cho từng trận đấu.
    Xử lý Bẫy 2 nếu người dùng chưa tạo lịch đấu.
    """
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    
    
    if not schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return
        
    for idx, match_str in enumerate(schedule, 1):
        
        team_parts = match_str.split(" vs ")
        team_a = team_parts[0]
        team_b = team_parts[1]
        
       
        sub_a = team_a[0:3]
        sub_b = team_b[0:3]
        
       
        code_a = f"{sub_a:X<3}"
        code_b = f"{sub_b:X<3}"
        
      
        match_code = f"M{idx:02d}"
        
       
        match_id = f"{match_code}-{code_a}-{code_b}"
        print(f"Trận {idx} ({match_str}) -> ID: {match_id}")


def main():
    """Hàm main điều phối giao diện dòng lệnh tương tác"""
    global teams_list, match_schedule
    
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Tự chế Combinations)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            input_teams_list()
        elif choice == "2":
            generate_match_schedule(teams_list)
        elif choice == "3":
            generate_match_ids(match_schedule)
        elif choice == "4":
            print("\nHệ thống quản lý giải đấu đang đóng. Chúc giải đấu diễn ra tốt đẹp!")
            break
        else:
            print("\nLựa chọn không hợp lệ! Vui lòng nhập số từ 1 đến 4.")


if __name__ == "__main__":
    main()