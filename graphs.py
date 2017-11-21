import constants
import utils

import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.data_array = []
        plt.ion()
        fig, self.graphs = plt.subplots(2, 2, sharex=True)

    def update(self, debug_info, error_info):
        new_point = utils.debug_line_to_dict(debug_info)
        if new_point is None:
            return

        # Keep only a certain amount of points
        if len(self.data_array) > constants.MAX_POINTS_PER_GRAPH:
            self.data_array = self.data_array[1:]

        self.data_array.append(new_point)
        self.draw()

    def draw(self):
        t = []
        cur_cell1 = []
        cur_cell2 = []
        cur_cell3 = []
        cur_cell4 = []
        eff = []
        temp_cell1 = []
        temp_cell2 = []
        temp_cell3 = []
        temp_cell4 = []
        temp_laser1 = []
        temp_laser2 = []
        temp_laser3 = []
        temp_laser4 = []

        for data in self.data_array:
            t.append(((int(data['timestamp'])-int(self.data_array[0]['timestamp']))/1000)-50)
            cur_cell1.append(data['current_cell1'])
            cur_cell2.append(data['current_cell2'])
            cur_cell3.append(data['current_cell3'])
            cur_cell4.append(data['current_cell4'])
            p_received = float(data['voltage_global']) * (float(data['current_cell1']) +
                                                               float(data['current_cell2']) +
                                                               float(data['current_cell3']) +
                                                               float(data['current_cell4']))
            p_sent = float(data['power_supply_voltage']) * float(data['power_supply_current'])
            if p_received != 0:
                eff.append(p_sent * 100 / p_received)
            else:
                eff.append(0)
            temp_cell1.append(data['temperature_cell1'])
            temp_cell2.append(data['temperature_cell2'])
            temp_cell3.append(data['temperature_cell3'])
            temp_cell4.append(data['temperature_cell4'])
            temp_laser1.append(data['temperature_laser1'])
            temp_laser2.append(data['temperature_laser2'])
            temp_laser3.append(data['temperature_laser3'])
            temp_laser4.append(data['temperature_laser4'])

        # Setup current graph
        self.graphs[0,0].clear()
        self.graphs[0,0].plot(t, cur_cell1, 'r')
        self.graphs[0,0].plot(t, cur_cell2, 'b')
        self.graphs[0,0].plot(t, cur_cell3, 'g')
        self.graphs[0,0].plot(t, cur_cell4, 'c')
        self.graphs[0,0].set_ylim([-0.05, 4])
        self.graphs[0,0].set_xlim([-50, 0])
        self.graphs[0,0].set_title("Courant dans les cellules")
        self.graphs[0,0].set_ylabel('Courant (A)')
        self.graphs[0,0].set_xlabel('Temps (s)')

        # Setup efficiency graph
        self.graphs[1,0].clear()
        self.graphs[1,0].plot(t, eff, 'r')
        self.graphs[1,0].set_ylim([-1, 100])
        self.graphs[1,0].set_xlim([-50, 0])
        self.graphs[1,0].set_title("Efficacite des cellules (P_envoye/P_recue)")
        self.graphs[1,0].set_ylabel('% Eff')
        self.graphs[1,0].set_xlabel('Temps (s)')

        # Setup temp cells
        self.graphs[0,1].clear()
        self.graphs[0,1].plot(t, temp_cell1, 'r')
        self.graphs[0,1].plot(t, temp_cell2, 'b')
        self.graphs[0,1].plot(t, temp_cell3, 'g')
        self.graphs[0,1].plot(t, temp_cell4, 'c')
        self.graphs[0,1].set_ylim([15, 80])
        self.graphs[0,1].set_xlim([-50, 0])
        self.graphs[0,1].set_title("Temperature des cellules")
        self.graphs[0,1].set_ylabel('Temperature degres C')
        self.graphs[0,1].set_xlabel('Temps (s)')

        # Setup temp laser graph
        self.graphs[1,1].clear()
        self.graphs[1,1].plot(t, temp_laser1, 'r')
        self.graphs[1,1].plot(t, temp_laser2, 'b')
        self.graphs[1,1].plot(t, temp_laser3, 'g')
        self.graphs[1,1].plot(t, temp_laser4, 'c')
        self.graphs[1,1].set_ylim([15, 80])
        self.graphs[1,1].set_xlim([-50, 0])
        self.graphs[1,1].set_title("Temperature des lasers")
        self.graphs[1,1].set_ylabel('Temperature degres C')
        self.graphs[1,1].set_xlabel('Temps (s)')

        plt.pause(0.1)
        plt.draw()
