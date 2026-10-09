#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    double dt = 0.01;
    double t_max = 100.0;
    
    double v_rest = -70.0;
    double v_reset = -75.0;
    double v_thresh = -55.0;
    double v_spike = 30.0;
    
    double tau = 10.0;
    double ref_period = 0.1;
    double t_ref = 0.0;
    
    double v = v_rest;
    
    ofstream outfile("data/ket_qua_mo_phong.csv");
    if (!outfile.is_open()) {
        cerr << "Error: Cannot open file." << endl;
        return 1;
    }
    
    outfile << "Time(ms),Voltage(mV)\n";

    for (double t = 0; t <= t_max; t += dt) {
        outfile << t << "," << v << "\n";

        double I_stim = (t >= 20.0 && t <= 80.0) ? 2.5 : 0.0;

        if (t_ref > 0.0) {
            v = v_reset;
            t_ref -= dt;
        } else {
            double dv = (-(v - v_rest) + I_stim * 10.0) / tau * dt;
            v += dv;

            if (v >= v_thresh) {
                v = v_spike;
                t_ref = ref_period;
            }
        }
    }

    outfile.close();
    return 0;
}