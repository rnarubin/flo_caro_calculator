# this is a comment in python

medida_palo=input('promt')

#Define volume function

#Length=3
#Vol_sys= A_tri()+A_rect+A+trap
base_tra = 0.50
height_tra = 0.255
base_rec = 1.62
height_rec = 0.28
height_tri = 0.34
base_half_tri=base_rec/2
limit_h_rec = height_tri+height_rec
limit_h_tra = limit_h_rec + height_tra

def A_tri():  
	#define variable values for traingle area calculations

	 # deinfe value for triangle height 
	if medida_palo <= 0.34
		base_tri=X*base_half_tri/height_tri
	else
		base_tri = 0.34

	#compute triangle area
	return base_tri*medida_palo
	
def A_rect

	#define	variable values for rectangle area calculations
	
	
	if medida_palo <= 0.34
		height_rec_x = 0
	else if medida_palo <= limit_h_rec
		height_rec_x = medida_palo - limit_h_rec
	else
		height_rec_x = 0.28
		
	#compute rectangle area
	return base_rect*height_rec_x

def A_trap
	#define	variable values for trapezoid area calculations
	
	 =  limit_h_rec + 
	#define height_trap
	if medida_palo <= limit_h_rec
		height_tra_x = 0
	else if medida_palo < 
		height_tra_x = medida_palo - 
	else medida_palo =>  
	
	return height_trap*(base_rect+base_trap)/2

