function BUBBLESORT(ARRAY)							            (1)
    # loop through the array multiple times
    loop INDEX from 0 to size of ARRAY – 1					    (2)
        # consider every pair of elements except the sorted ones
        loop INDEX2 from 0 to size of ARRAY – 2 – INDEX			(3)
            if ARRAY[INDEX2] > ARRAY[INDEX2 + 1] then			(4)
                # swap elements if they are out of order
                TEMP = ARRAY[INDEX2]						    (5)
                ARRAY[INDEX2] = ARRAY[INDEX2 + 1]				(6)
                ARRAY[INDEX2 + 1] = TEMP					    (7)
            end if
        end loop
    end loop
end function


function QUICKSORT(ARRAY, START, END)			(1)
    # base case size <= 1		
    if START >= END then					    (2)		
        return						            (3)
    end if							            (4)
    PIVOTINDEX = PARTITION(ARRAY, START, END)	(5)
    QUICKSORT(ARRAY, START, PIVOTINDEX – 1)		(6)
    QUICKSORT(ARRAY, PIVOTINDEX + 1, END)		(7)
end function