#!/usr/bin/env python

def list_to_strln(input_list):
    output_str = str(input_list)
    output_str = output_str[1:(len(output_str) - 1)] + '\n'
    output_str = output_str.replace("'", "")
    return output_str

read_filename = 'legdam10_parsed.txt'
f = open(read_filename, 'r')

#   Assume the shortest note is an eighth note
atom_note = 8

#   Read in melody as a sequence of atom notes
sequence = []

clocks_per_QN = 120
track = 4
channel = 2
velocity = 100

for line in f:
    pitch = int(line)
    sequence.append(pitch)
    
f.close()

write_filename = 'legdam10_generated.csv'
f = open(write_filename, 'w')

current_pitch = sequence[0]
duration = 0
start_time = 0
end_track_time = 0
for pitch in sequence:
    if pitch == current_pitch:
        duration = duration + clocks_per_QN*4/atom_note
    else:
        line1 = [track, start_time, 'Note_on_c', channel, current_pitch, velocity]
        f.write(list_to_strln(line1))
        
        line2 = [track, start_time + duration, 'Note_on_c', channel, current_pitch, 0]
        f.write(list_to_strln(line2))
        
        start_time = start_time + duration
        end_track_time = start_time
        duration = clocks_per_QN*4/atom_note
        current_pitch = pitch
        
end_track_line = [track, end_track_time, 'End_track']
f.write(list_to_strln(end_track_line))
f.close()

