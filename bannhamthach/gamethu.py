# #Thư viện pygame
# #Câu lệnh bắt buộc có khi setting pygame.
# import pygame
# import random 
# import sys
# # HÀM
# def laser_update(list_laser,laser_speed=10000):
#     for rect in list_laser:
#         rect.y -= laser_speed * delta_time
#         if rect.bottom<0:
#             list_laser.remove(rect)
# def meteor_update(list_meteor,meteor_speed=500):
#     for set_meteor in list_meteor:
#         positions = set_meteor[0] # Vector hướng di chuyển của hành tinh
#         meteor_rect = set_meteor[1]  # Hình chữ nhật đại diện cho hành tinh
#         meteor_rect.center += positions * meteor_speed *delta_time
#         # Kiểm tra nếu hành tinh ra khỏi phía dưới màn hình
#         if meteor_rect.bottom>dis_cao:
#            list_meteor.remove(set_meteor)
# ##Hàm hiển thị điểm 
# def Score_player(score_choi, score_show):
#     font_score1=pygame.font.Font("subatomic.ttf",20)
#     font_score2=pygame.font.Font("subatomic.ttf",40)
#     if running:
#         score_txt=font_score1.render(f'Score: {score_choi}',True,(65,105,255))#Print score lên màn hình
#         score_rect=score_txt.get_rect(midtop=(dis_rong/2,5))
#         screen.blit(score_txt,score_rect)#position hiển thị
#         pygame.draw.rect(screen,(65,105,255),score_rect.inflate(30,30), width=10 , border_radius = 5)
#     elif running==False:
#         score_txt1=font_score2.render(f'Your score: {score_show}',True,(0,255,0))#Print score lên màn hình
#         screen.blit(score_txt1,(450,360))#position hiển thị
#         hscore_txt=font_score2.render(f'High score: {hscore}',True,(0,255,0))
#         screen.blit(hscore_txt,(470,390))
#         note_txt=font_score2.render(f'Press space to play again!!!',True,(255,0,0))
#         screen.blit(note_txt,(300,300))     
# pygame.init()
# #BIẾN
# ## Tọa độ của thiên thạch
# x_pos=0
# y_pos=0
# score_choi=0
# score_show=0
# hscore=0#Điểm cao nhất
# bg_x=0
# ##Khởi tạo hàm điều chỉnh tốc độ hiển thị(điều khiển của user) của rắn  
# clock = pygame.time.Clock()
# previous_frame_time = pygame.time.get_ticks()
# FPS = 30
# ##Khởi tạo giá trị x ,y ban đầu để sử dụng di chuyển 
# dis_rong,dis_cao=1280,720
# #XỬ LÝ MÀN HÌNH GAME
# ##Tạo cửa số game và tiêu đề game
# screen=pygame.display.set_mode((dis_rong,dis_cao))
# pygame.display.set_caption("Game Bắn Nham Thạch")
# ##Tạo icon game
# # sử dung image.load để tải icon snake.png từ file theo path
# icon=pygame.image.load(r"meteor.png")
# pygame.display.set_icon(icon)
# # Hình ảnh của tàu vũ trụ
# rocket=pygame.image.load(r"rocket.png")
# rocket_rect=rocket.get_rect(center=(dis_rong//2, dis_cao-80 ))#để lấy hình chữ nhật (rectangle) bao quanh ảnh
# # Hình nền
# bg_chinh=pygame.image.load(r"background.png")
# # Hình đạn laser
# laser=pygame.image.load(r"laser.png")
# list_laser=[] 
# # Hình thiên thạch 
# meteor=pygame.image.load(r"asteroid.png")
# list_meteor=[]
# # Bộ đếm thời gian ngắn để tạo sự kiện tạo thiên thạch mới 
# meteor_time=pygame.event.custom_type() # Tạo một kiểu sự kiện tùy chỉnh để kích hoạt sự kiện tạo hành tinh mới
# pygame.time.set_timer(meteor_time,500) # Thiết lập một bộ đếm thời gian 
# ##Vòng lặp xử lý hiển thị game
# ###Tạo biến running để kiểm tra xem game còn chạy hay dừng rồi
# running=True # Ban đầu không chạy game
# while True :
#     #cho biết thông tin về hành động của user từ hàm event.get() diễn ra trên màn hình 
#     for event in pygame.event.get():
#         #nếu người dùng click nút thoát(x) trên cửa sổ game thì dừng game 
#         if event.type==pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_SPACE:#Nếu bấm space thì sẽ chơi lại 
#                    running=True
#         if running :
#             if event.type==pygame.MOUSEBUTTONDOWN:
#                 laser_rect=laser.get_rect(midbottom=rocket_rect.midtop)
#                 list_laser.append(laser_rect)
#             if event.type == meteor_time:
#                 # Random vị trí 
#                 x_pos=random.randint(0,1280)
#                 y_pos=random.randint(0,600)
#                 meteor_rect=meteor.get_rect(center=(x_pos,y_pos))
#                 positions=pygame.math.Vector2(random.uniform(-0.2,0.2),1)
#                 list_meteor.append((positions,meteor_rect))
#             delta_time = (pygame.time.get_ticks() - previous_frame_time) / 1000.0 / FPS	 #Cập nhật vị trí của các hành tinh và lasers một cách nhất quán và dựa trên thời gian và giúp trò chơi của bạn hoạt động trơn tru và chính xác hơn
#             previous_frame_time = pygame.time.get_ticks()
#             # Di chuyển tàu theo con trỏ chuột
#             rocket_rect.center = pygame.mouse.get_pos()
#             # Vẽ tất cả trên màn hình   
#             ##di chuyển background từ phải về trái tới lề bên trái là -800 thì gán bg_x=0 để thực hiện nối thêm background vào game
#             bg_x-=1
#             ##vẽ đối tượng lên trên màn hình dùng blit
#             screen.blit(bg_chinh,(bg_x,0))
#             ##xử lý background chạy vô tận
#             if(bg_x==-800):
#                 bg_x=0
#             screen.blit(bg_chinh,(bg_x+800,0))  
#             # Cập nhật lại màn hình 
#             laser_update(list_laser)
#             meteor_update(list_meteor)
#             # Xử lý va chạm khi laser chạm vào thiên thạch
#             for laser_rect in list_laser:
#                 for set_meteor in list_meteor:
#                     if laser_rect.colliderect(set_meteor[1]):
#                         list_laser.remove(laser_rect)
#                         list_meteor.remove(set_meteor)
#                         score_choi+=1
#             score_show=score_choi
#             if score_choi>hscore:
#                 hscore=score_choi
#             # Xử lý va chạm khi tàu chạm vào thiên thạch
#             for set_meteor in list_meteor:
#                 if rocket_rect.colliderect(set_meteor[1]):
#                     running=False
#             # Vẽ đạn 
#             for rect in list_laser:
#                 screen.blit(laser, rect)
#             # Vẽ nham thạch
#             for set_meteor in list_meteor:
#                 screen.blit(meteor, set_meteor[1])
#             # Vẽ tàu
#             screen.blit(rocket, rocket_rect)
#             Score_player(score_choi,score_show)
#             clock.tick(FPS)
#         else:
#             #reset lại game
#             #khởi tạo lại
#             x_pos=0
#             y_pos=0
#             score_choi=0
#             list_laser=[]
#             list_meteor=[]
#         pygame.display.update()
    

        
                
# Hiển thị màn hình game
screen.blit(bg_chinh, (0, bg_y))
# Hiển thị tàu vũ trụ
screen.blit(rocket, rocket_rect)
# Hiển thị đạn laser
for rect in list_laser:
    screen.blit(laser, rect)
# Hiển thị thiên thạch
for set_meteor in list_meteor:
    screen.blit(meteor, set_meteor[1])
     
