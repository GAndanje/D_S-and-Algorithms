#solution 1 for min_letters_to_del
def min_letters_to_del_1(S,memoir={}):
    """The memoir object keeps track of the number of times a character 'x' appears in the string"""
    if not len(S):#checks wether the string is empty
        return 0
    for i in S:
        if not i in memoir:#if character key not in {memoir} object create one
            memoir[i]=1
        else:#otherwise increment count
            memoir[i]+=1
    count=0#count for all characters appearing an odd numvber of times
    for k in memoir.values():
        if k%2!=0:#if character apppears odd number of times 
            count+=1
    return count

# TODO uncomment the print statements below to call the functions and print results in the console
# print(min_letters_to_del_1('acbcbba'))

#alternative solution for min_letters_to_del
def min_letters_to_del_2(S,memoir={}):
    """memoir keeps track of the number of times a character 'x' appears in the string"""
    if not len(S):
        return 0
    for i in S:
        if not i in memoir:
            memoir[i]=1
        else:
            memoir[i]+=1
    return len(list(filter(lambda x:x%2!=0,memoir.values())))

# TODO uncomment the print statements below to call the functions and print results in the console
# print(min_letters_to_del_2('acbcbba'))

def largest_two_frags(S,memoir={}):
    """
    The memo will keep track of the {second_largest}
    fragment and the {largest_sum_of_two} fragments for each iteration
    """
    left_slice=''#to hold the string slice to the left of the current fragment
    right_slice=''#to hold the string slice to the right of the current fragment
    current_fragment=''
    memoir['largest_sum_of_two_fragments']='00'
    
    #Top level iteration|first iteration
    for i in range(len(S)-1):
        current_fragment=S[i]+S[i+1]
        left_slice='' if i == 0 else S[:i]
        right_slice='' if i >len(S)-2 else S[i+2:]
        get_second_fragment_helper(left_slice,right_slice,memoir)
        if int(current_fragment)+int(memoir['helper_largest'])>int(memoir['largest_sum_of_two_fragments']):
            memoir['largest_sum_of_two_fragments']=int(current_fragment)+int(memoir['helper_largest'])
    return int(memoir['largest_sum_of_two_fragments']),current_fragment,memoir['helper_largest']

def get_second_fragment_helper(left_slice,right_slice,memoir):
    """
    This function performs the second iteration.Call it the inner or 
    nested iteration to return the {second_largest_fragment} by comparing 
    the left and right slices e.g if current_fragment is '65' in a string 
    S='143657' left_slice is '143' right_slice is '7' thus it should update 
    43 as the {second_largest_fragment} in the {memoir}
    """
    memoir['helper_largest']='00'
    #return the largest on the left slice
    if left_slice != '' and len(left_slice)>1:
        if len(left_slice)==2 and int(left_slice)>int(memoir['helper_largest']):
            memoir['helper_largest']=left_slice
        for i in range(len(left_slice)-2):
            if int(left_slice[i]+left_slice[i+1])>int(memoir['helper_largest']):
                memoir['helper_largest']=left_slice[i]+left_slice[i+1]
    #return the largest on the right slice
    if right_slice != '' and len(right_slice)>1:
        if len(right_slice)==2 and int(right_slice)>int(memoir['helper_largest']):
            memoir['helper_largest']=right_slice
        for i in range(len(right_slice)-2):
            if int(right_slice[i]+right_slice[i+1])>int(memoir['helper_largest']):
                memoir['helper_largest']=right_slice[i]+right_slice[i+1]
                
# TODO uncomment the print statements below to call the functions and print results in the console
# print(largest_two_frags('43798'))
            
        
