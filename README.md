# Prime number finder

Simple project to see now many prime numbers can be found using a low-powered machine. The target machine is a [Ramnode OpenVZ SSD with 128MB physical RAM and 64MB swap](http://www.ramnode.com/vps.php).

The attempt envisages that the target machine will crash due to memory issues, so the script is written to write prime numbers to a file, so that it can easily be restarted.

## Technology overview
The script uses pure python with no modules or dependencies.

## Set-up
```
# Clone this repository
https://github.com/dalepotter/prime-number-finder.git

# Run the script
python get_primes.py
```

## Automating restarts
It is envisaged that the target machine will crash periodically, so the script can be set to restart on reboot using cron (after a 60 second delay):
```
@reboot sleep 60 && python get_primes.py
```
