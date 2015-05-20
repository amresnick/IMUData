import csv
import itertools
import time


def number_of_measurements(file_name):
    ifile = open(file_name, 'r')
    reader = csv.reader(ifile)
    total = 0

    for row in reader:
        total += 1
    ifile.close()
    return total


def write_first_x_hours_of_data(hours, read_file, write_file, sample_rate):
    num_rows = hours*60*60*sample_rate

    ifile = open(read_file, 'r')
    reader = csv.reader(ifile)
    ofile = open(write_file, 'w')
    writer = csv.writer(ofile)

    for row in itertools.islice(reader, num_rows):
        writer.writerow(row)

    ifile.close()
    ofile.close()


def integrate_sensor_data(sensor_select, read_file, write_file, sample_rate):
    ifile = open(read_file, 'r')
    reader = csv.reader(ifile)
    ofile = open(write_file, 'w')
    writer = csv.writer(ofile)

    val = 0
    count = 0
    buf = []
    row_to_write = []
    row_to_write.append(0)
    for row in reader:
        if (count == 0):
            buf.append(row[sensor_select])
            count += 1
        else:
            buf.append(row[sensor_select])
            buf = map(float, buf)
            val += (buf[0] + buf[1])*(1/sample_rate)*.5
            row_to_write[0] = val
            del buf[0]
            writer.writerow(row_to_write)
            count += 1

    ofile.close()
    ifile.close()
    return(count)


# write_first_x_hours_of_data(12, 'imuData.csv', '12HoursIMU.csv', 100)
# total = number_of_measurements('testing.csv')
integrate_sensor_data(0, '12HoursIMU.csv', 'angles.csv', 100.0)


"""Takes a csv file where each column of data is a sensor.
A new csv called computation.csv is then output
where the data is split into bins.
Each row is a different bin.
This is not very efficient as we are looping through
the data source file a lot of times"""


def allan_data_reshape(sample_freq, totalTimeHours, sensor_select):
    # sensor_select = 0  # Which column (sensor) to work with
    # sample_freq = 100 # Hz
    # totalTimeHours = 2
    totalTimeSec = totalTimeHours * 60 * 60
    # Need at least 9 bins for significance
    maxBinSize = (totalTimeSec/9) * sample_freq
    maxBinSize += 1

    # Open the file
    ifile = open('testing.csv', 'r')
    reader = csv.reader(ifile)
    ofile = open('computation.csv', 'w')
    writer = csv.writer(ofile)

    # Create all of the data bins
    print 'Starting loops...'
    for binLength in xrange(1, 4):
        offset = time.time()
        print 'Loop', binLength, 'of', maxBinSize
        count = 1
        write_row = []
        # Iterate through the data file
        for row in reader:
            # put value into list and write it out
            if (not(count % binLength)):
                write_row.append(row[sensor_select])
                writer.writerow(write_row)
                write_row = []
                count += 1
            else:
                # put value into list,
                # but there are more of them, so don't write it out yet
                write_row.append(row[sensor_select])
                count += 1
        ifile.seek(0)
        end_time = time.time() - offset
        print 'Took', end_time, 'seconds'

    # Close all files
    ifile.close()
    ofile.close()

# allan_data_reshape(100, 13, 0)
