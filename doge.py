#!/usr/bin/python
# coding: utf-8

import getpass, time, requests, sys
from random import randint
from colorama import init, Fore, Back, Style
from optparse import OptionParser
init()

splash = u'''
 █████╗  █████╗  █████╗   ██████╗ ██╗ ██████╗███████╗██████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
╚██████║╚██████║╚██████║  ██║  ██║██║██║     █████╗  ██████╔╝██║   ██║   ██║   
 ╚═══██║ ╚═══██║ ╚═══██║  ██║  ██║██║██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
 █████╔╝ █████╔╝ █████╔╝  ██████╔╝██║╚██████╗███████╗██████╔╝╚██████╔╝   ██║   
 ╚════╝  ╚════╝  ╚════╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   
                                                                               '''
key = 'ee0c7f7e43e346b3841994a8e4501077'
bet = [(0, 900000), (99999, 999999)]
ka = "100000000"
user = "Rma691"
paswd= "kapten691"
curency = "Doge"
ch = 90
ch2 = 49
mult = 2

parser = OptionParser()
parser.add_option("-u", "--Username", type="string",
                  help="username on 999dice.com")
parser.add_option("-p", "--Password", type="string")
parser.add_option("-P", "--PayIn", type="string",
                  help="your minimal bet")
parser.add_option("-M", "--MaxPayIn", type="int", default=0,
                  help="The maximum bet amount, or 0 for no maximum. (default=0) in satoshis")
parser.add_option("-S", "--StopMinBalance", type="int", default=0,
                  help="After a bet, if your balance is less than this amount, then stop betting. (default=0) in satoshis")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print most messages to stdout")

(options, args) = parser.parse_args()
class MakeVars(object):
    def __init__(self, data):
        for key, val in data.items():
            setattr(self, key, val)


def request_api(data):
    for attempt in range(20):
        try:
            r = requests.post('https://www.999dice.com/api/web.aspx', data=data)
            #print 'Waiting.........!!!!'
            #print r.text
            return MakeVars(r.json())
        except requests.exceptions.ConnectionError as error:
            print (Fore.RED + 'Connection error')
            if not attempt == 9:
                print (Fore.RED + 'retrying...')
            else:
                print (Fore.RESET + 'Connection error. Details: ' + str(error))
                sys.exit()


class Bot(object):
    def __init__(self, key):
        self.Key = key
        self.Totp = None
        if options.Username and options.Password:
            self.Username = user
            self.Password = paswd
        else:
            try:
                self.Username = user
                self.Password = paswd
            except:
                self.Username = raw_input('Username:')
                self.Password = getpass.getpass('Password:')
        if curency != None:
            self.currency = curency
        else:
            self.currency = raw_input('select currency Doge/LTC/ETH: ')
        self.chance = float(raw_input('Chance:'))
        self.chance1 = float(raw_input('Chance2:'))
        self.PayIn_origin1 = float(raw_input('Base bet:'))
        self.PayIn1 = float(raw_input('Bet size:'))
        highbet = 1000000-((1000000*int(self.chance))/100)
        lowbet = 999999-(1000000-((1000000*int(self.chance))/100))
        self.bet = [(0, lowbet), (highbet, 999999)]
        highbet1 = 1000000-((1000000*int(self.chance1))/100)
        lowbet1 = 999999-(1000000-((1000000*int(self.chance1))/100))
        self.bet1 = [(0, lowbet1), (highbet1, 999999)]
        self.multi = int(float(raw_input('Martingle:')))
        self.PayIn_origin = int(self.PayIn_origin1 * 100000000)
        self.PayIn = int(self.PayIn1 * 100000000)
    def login(self):
        data = dict(
            a = 'Login',
            Key = self.Key,
            Username = self.Username,
            Password = self.Password,
            )
        #print data
        self._ = request_api(data)

    def login1(self):
        data = dict(
            a = 'Login',
            Key = self.Key,
            Username = self.Username,
            Password = self.Password,
            Totp = self.Totp,
            )
        #print data
        self._ = request_api(data)
        

    def get_balance(self):
        data = dict(
            a = 'GetBalance',
            s = self._.SessionCookie,
        )
        #print data
        r = request_api(data)
        #print float(r.Doge['Balance'] * aa)
        self._.Balance = r.Balance
        print 'You balance:', float(self._.Doge['Balance'] * aa),
        
    def place_bet(self, b):
        data = dict(
            a = 'PlaceBet',
            s = self._.SessionCookie,
            PayIn = self.PayIn,
            Low = self.bet[b][0],
            High = self.bet[b][1],
            Currency = self.currency,
        )
        r = request_api(data)
        #print r.text
        self.__ = r
        self._.PayOut = r.PayOut

    def waktu(self, secs):
        mins, secs = divmod(secs,60) 
        hours, mins = divmod(mins,60) 
        return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs) 


    def place_bet1(self, b):
        data = dict(
            a = 'PlaceBet',
            s = self._.SessionCookie,
            PayIn = self.PayIn,
            Low = self.bet1[b][0],
            High = self.bet1[b][1],
            Currency = self.currency,
        )
        r = request_api(data)
        #print r.text
        self.__ = r
        self._.PayOut = r.PayOut

    def place_bet3(self, b):
        data = dict(
            a = 'PlaceBet',
            s = self._.SessionCookie,
            PayIn = self.PayIn,
            Low = self.bet1[b][0],
            High = self.bet1[b][1],
            Currency = self.currency,
        )
        r = request_api(data)
        #print r.text
        self.__ = r
        self._.PayOut = r.PayOut
        
    def place_auto_bet(self, b):
        data = dict(
            a = 'PlaceAutomatedBets',
            s = self._.SessionCookie,
            BasePayIn = self.PayIn,
            Low = bet[b][0],
            High = bet[b][1],
            MaxBets = 1,
            ResetOnWin = True,
            IncreaseOnLosePercent = 1,
            MaxPayIn = options.MaxPayIn,
            StopOnLoseMaxBet = True,
            StopMinBalance = options.StopMinBalance,
            Currency = self.currency,
            Compact = True
        )
        r = request_api(data)
        self.ab = r

def main():
    print(Fore.YELLOW + Style.BRIGHT + splash)
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    
    bot = Bot(key)
    try:
        bot.login()
        bot._.Balance_origin = bot._.Doge['Balance']
    except:
        bot.Totp = int(raw_input('2FA:'))
        bot.login1()
        bot._.Balance_origin = bot._.Doge['Balance']
    
    #print '1 Satoshi = 0.0000001 DOGE'
    print 'You balance:', str(float(bot._.Doge['Balance']*0.00000001)), ' ', str(bot.currency)
    
    """if options.PayIn:
        pay_in = options.PayIn
    else:
        pay_in = raw_input('Pay in (default:1 satoshis):')
    if pay_in.isdigit() and int(pay_in) != 1:
        bot.PayIn_origin = bot.PayIn = int(pay_in)
    
    print 'Here we go'
    """
    lose_count = 0
    win_count = 0
    lose = 0
    win = 0
    win_bet = 0
    lose_bet = 0
    timer = time.time()
    while True:
        try:
            aa = 0.00000001
            bot._.Balance = bot._.Doge['Balance'] * aa
            b = randint(0, len(bet)-1)
            if win_count > 0:
                bot.place_bet(b)
                print(Back.WHITE + Fore.RED + 'Chance: ' + str(float(bot.chance)) + ' %                                 ')      
            elif lose_count > 1:
                bot.place_bet1(b)
                print(Back.WHITE + Fore.RED + 'Chance: ' + str(float(bot.chance1)) + ' %                               ')      
            else:
                bot.place_bet1(b)
                print(Back.WHITE + Fore.RED + 'Chance: ' + str(float(bot.chance1)) + ' %                               ')      
            result = bot._.PayOut - bot.PayIn
            result1 = (bot._.PayOut - bot.PayIn) * aa
            balance = (bot.__.StartingBalance + result) * aa
            profit =  balance - bot._.Balance
            amount = bot.PayIn * aa
            balance2 = bot._.Balance + profit
            #if lose_count == 1:
                #print (Back.YELLOW + Fore.RED + 'Lose ' + str(lose_count) + ' times. Back to minimal.')
                #result = 0

            if result < 0:
                win_count = 0
                lose_count += 1
                if lose < lose_count:
                    lose = lose_count
                else:
                    lose = lose
                bot.PayIn = bot.PayIn*bot.multi
                if lose_bet < amount:
                    lose_bet = amount
                else:
                    lose_bet = lose_bet
                print(Back.RED + Fore.WHITE)
            else:
                lose_count = 0
                win_count += 1
                if win < win_count:
                    win = win_count
                else:
                    win = win
                bot.PayIn = bot.PayIn_origin
                if win_bet < amount:
                    win_bet = amount
                else:
                    win_bet = win_bet
                print(Back.GREEN + Fore.WHITE + Style.BRIGHT)
                
            if options.verbose:
                timing = time.time() - timer
                print(bot.waktu(timing) + '  \n')
                print('Bet amount: ' + str(float(amount)) + ' ' + str(bot.currency) + '  ')
                print('Profit: ' + str(float(result1)) + ' ' +  str(bot.currency) + '  ')
                print('high win bet amount: ' + str(float(win_bet)) + ' ' + str(bot.currency) + '  ')
                print('high lose bet amount: ' + str(float(lose_bet)) + ' ' + str(bot.currency) + '  ')
                if win_count > 0:
                    print('Current streak : ' + str(win_count) + '  ')
                else:
                    print('Current streak : ' + str(lose_count) + '  ')
                print('Win streak : ' + str(win) + '  ')
                print('Lose streak : ' + str(lose) + '  ')
                print('Balance awal: ' + str(float(bot._.Balance)) + ' ' + str(bot.currency) + '  ')
                print('Current Profit : ' + str(float(profit)) + ' ' + str(bot.currency) + '  ')
                print('Balance akhir : ' + str(float(balance2)) + ' ' + str(bot.currency) + '  ')
                print(Fore.RESET + Back.RESET + Style.RESET_ALL)
            
        except KeyboardInterrupt:
            print(Fore.YELLOW + Style.BRIGHT +'='*80)
            print(Fore.RESET + Back.RESET + Style.RESET_ALL + 'You have earned: ' + str(bot._.Balance-bot._.Balance_origin) + ' satoshis')
            break
    
    bot.get_balance()
    print "Bye"
    sys.exit()

if __name__ == '__main__':
    main()

# EOF