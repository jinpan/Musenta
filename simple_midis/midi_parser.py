#!/usr/bin/env python

read_filename = 'legdam10_simple.csv'
f = open(read_filename, 'r')

#   Assume the shortest note is an eighth note
atom_note = 8

#   Store melody as a sequence of atom notes
sequence = []

clocks_per_QN = 120

prev_end_time = 0
for line in f:
    line = line.split(',')
        
    if ' Note_on_c' in line:
        time = int(line[1])
        pitch = int(line[4])
        velocity = int(line[5])
        
        if velocity != 0:
            #   Begin pitch
            sequence.append(pitch)
        elif velocity == 0:
            #   End pitch
            start_time = prev_end_time
            end_time = time
            num_atom_notes = (end_time - start_time)/(clocks_per_QN/(atom_note/4))
            for i in xrange(num_atom_notes - 1):
                sequence.append(pitch)
            prev_end_time = end_time
                
f.close()

write_filename = 'legdam10_parsed.txt'
f = open(write_filename, 'w')
for pitch in sequence:
    f.write(str(pitch) + '\n')
f.close()
