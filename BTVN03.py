import itertools


teams_list = []
match_schedule = []

def input_teams_list():
    """
    Chức năng 1: Nhập và chuẩn hóa danh sách đội.

    """
    global teams_list
    print("\n--- NHẬP DANH SÁCH ---")
    user_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    
    
    raw_list = [team.strip().upper() for team in user_input.split(",") if team.strip()]
    
    
    teams_list = list(dict.fromkeys(raw_list))
    
    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

def generate_match_schedule():
    """
    Chức năng 2: Tạo lịch thi đấu vòng tròn .
    
    """
    global match_schedule, teams_list
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    
    
    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        match_schedule = []
        return
        
    
    combos = itertools.combinations(teams_list, 2)
    match_schedule = [f"{a} vs {b}" for a, b in combos]
    
    # In kết quả
    for idx, match in enumerate(match_schedule, 1):
        print(f"{idx}. {match}")
        
    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

def generate_match_ids():
    """
    Chức năng 3: Tạo mã ID cho trận đấu.
    Sử dụng F-String với định dạng 02d và padding X<3.
    """
    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return
        
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    for idx, match in enumerate(match_schedule, 1):
     
        team_a, team_b = match.split(" vs ")
        
        
        code_a = f"{team_a[:3]:X<3}"
        code_b = f"{team_b[:3]:X<3}"
        
     
        match_id = f"M{idx:02d}-{code_a}-{code_b}"
        print(f"Trận {idx} ({match}) -> ID: {match_id}")

def main():

    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động")
        print("4. Đóng hệ thống")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            input_teams_list()
        elif choice == "2":
            generate_match_schedule()
        elif choice == "3":
            generate_match_ids()
        elif choice == "4":
            print("Kết thúc . Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()