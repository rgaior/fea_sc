tmux new-session -d -s caencontrol;  # start new detached tmux session, run htop
tmux send-keys "source /home/xenon/slowcontrol/sc_venv/bin/activate";
tmux send-keys Enter;
tmux split-window -v -p 50
tmux send-keys "source /home/xenon/slowcontrol/sc_venv/bin/activate";
tmux send-keys Enter;

tmux split-window -h -p 50
tmux send-keys "source /home/xenon/slowcontrol/sc_venv/bin/activate";
tmux send-keys Enter;

tmux select-pane -t 0
tmux split-window -h -p 50
tmux send-keys "source /home/xenon/slowcontrol/sc_venv/bin/activate";
tmux send-keys Enter;

tmux select-pane -t 0
tmux send-keys "screen -S caen1_control python -i caendt55/sc_caendt55.py caen1";
tmux send-keys Enter;

tmux select-pane -t 2
tmux send-keys "screen -S caen2_control python -i caendt55/sc_caendt55.py caen2";
tmux send-keys Enter;

tmux select-pane -t 1
tmux send-keys "sleep 10 " ;
tmux send-keys Enter;
tmux send-keys "screen -S caen1_display python -i caendt55/caen_display.py sc/hv/caen1/get";
tmux send-keys Enter;

tmux select-pane -t 3
tmux send-keys "sleep 10 " ;
tmux send-keys Enter;
tmux send-keys "screen -S caen2_display python -i caendt55/caen_display.py sc/hv/caen2/get";
tmux send-keys Enter;


#tmux send-keys "echo 2" C-m
#tmux split-window -h -p 50
#tmux send-keys "echo 3" C-m


# tmux new-session -d -s htop-session 'htop';  # start new detached tmux session, run htop
# tmux split-window;                             # split the detached tmux sessiont
# tmux send-keys "sleep 2 " \;
# tmux send-keys Enter;                     # send 2nd command 'htop -t' to 2nd pane. I believe there's a `--target` option to target specific pan.
# tmux send-keys "python update_line.py " \;
# #tmux send-keys "sleep 2 " \;
# tmux send-keys Enter;                     # send 2nd command 'htop -t' to 2nd pane. I believe there's a `--target` option to target specific pan.
# tmux a;                                        # open (attach) tmux session.
