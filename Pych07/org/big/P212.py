'''
Created on 2024. 12. 4.

@author: user
'''
import operator;

trainDIc, trainList = {}, [];

trainDIc = {'Tomas':'토마스', 'Edward':'에드워드', 'Henry':'헨리', 'Gothen':'고든', 'James':'제임스'};
trainList = sorted(trainDIc.items(), key = operator.itemgetter(1));

print(trainList);