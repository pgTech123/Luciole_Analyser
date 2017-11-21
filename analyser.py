import os
import sys
import graphs


DEBUG_LOG_FILE = "/debug_log.csv"
ERROR_LOG_FILE = "/error_log.csv"


def read_new_content(f):
    return f.readline()


def main(program_path):
    graph = graphs.Graph()
    print "Starting the analyser"
    path = os.getcwd() + '/' + program_path

    running = 1
    debug_file = open(path + DEBUG_LOG_FILE, 'r')
    error_file = open(path + ERROR_LOG_FILE, 'r')
    debug_file.seek(0, 2)   # Go to the end of file (we don't care about the past)

    while running:
        new_debug_line = read_new_content(debug_file)
        new_error_line = read_new_content(error_file)

        if new_debug_line or new_error_line:
            # Do not care about labels
            if not new_debug_line.startswith("Timestamp"):
                graph.update(new_debug_line, new_error_line)

    print "Shutting down"


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) is not 1:
        print "You must specify where the UI logs are"
        sys.exit(0)
    main(argv[0])
