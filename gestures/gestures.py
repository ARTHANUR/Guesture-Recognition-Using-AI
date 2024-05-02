from .positions import *
face,pose,left,right='face','pose','lh','rh'

__all__=['iLoveYou','father','mother','house','hello','thanks','you','sorry','no' ,'chill','notWell','name','thumbsUp','thumbsDown']

@handler
def chill(dots):
    if (bool(dots['rh']) and right_thumb_open(dots) and right_fore_finger_up(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_up(dots)):
        return True
    return False

@handler
def father(dots):
    return openRightFist(dots) and dots[face]['151']['x']==dots[right]['4']['x']

@handler
def mother(dots):
    if openRightFist(dots) and intersect(dots,right,4,face,152):
        return True
    return False

@handler
def house(dots):
    if openLeftFist(dots) and openRightFist(dots) and intersect(dots,left,12,right,12) and abs(dots[right]['0']['x']-dots[left]['0']['x'])>80 and abs(dots[left]['7']['x']-dots[left]['15']['x'])<=10 and abs(dots[right]['7']['x']-dots[right]['15']['x'])<=10:
        return True
    
@handler
def hello(dots):
    return openRightFist(dots) and intersect(dots,face,70,right,8)

@handler
def thanks(dots):
    return openLeftFist(dots) and openRightFist(dots) and intersect(dots,left,12,right,12) and intersect(dots,left,12,face,13) and abs(dots[left]['4']['x']-dots[right]['4']['x'])>80 

@handler
def you(dots):
    if (bool(dots['rh']) and right_thumb_closed(dots) and right_fore_finger_up(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_down(dots)  ):
        return True
    return False

@handler
def sorry(dots):
    if(bool(dots['pose']) and bool(dots[right]) and closedRightFist(dots) and intersect(dots,pose,22,pose,11,50)) and not intersect(dots,pose,12,pose,21,50):
        return True
    
@handler
def no(dots):
    if(bool(dots['pose']) and bool(dots[right]) and bool(dots[left]) and closedLeftFist(dots) and closedRightFist(dots) and intersect(dots,pose,12,pose,21,50) and intersect(dots,pose,22,pose,11,50)):
        return True
    
@handler
def iLoveYou(dots):
    if(bool(dots['pose']) and bool(dots[left]) and right_thumb_open(dots) and right_fore_finger_up(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_down(dots) and intersect(dots,left,6,left,3,50) ):
        return True
# iLoveyou Is Not Working

@handler
def notWell(dots):
    return openLeftFist(dots) and openRightFist(dots) and intersect(dots,left,12,right,12) and intersect(dots,left,12,face,10) and abs(dots[left]['4']['x']-dots[right]['4']['x'])>80 

@handler
def name(dots):
    return right_thumb_closed(dots) and right_fore_finger_down(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_up(dots) and intersect(dots,right,20,face,61) 

@handler
def yes(dots):
    return left_thumb_open(dots) and left_fore_finger_up(dots) and left_middle_finger_down(dots) and left_ring_finger_down(dots) and left_small_finger_down(dots) and right_thumb_open(dots) and right_fore_finger_up(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_down(dots)   
# yes is not working

@handler
def thumbsUp(dots):
    return right_thumb_up(dots) and right_fore_finger_down(dots) and right_middle_finger_down(dots) and right_ring_finger_down(dots) and right_small_finger_down(dots)

@handler
def thumbsDown(dots):
    return left_thumb_down(dots) and left_fore_finger_down(dots) and left_middle_finger_down(dots) and left_ring_finger_down(dots) and left_small_finger_down(dots)
# thumbsDown is not working

@handler
def temple(dots):
    return openLeftFist(dots) and openRightFist(dots) and intersect(pose,left,12,right,12)