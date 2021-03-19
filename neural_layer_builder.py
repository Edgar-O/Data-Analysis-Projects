
def layer_combo(num_layers, neurons_per_layer):
    import itertools
    df = []
    layers = []
    iter_layer = 0
    while iter_layer < num_layers:
        layers.append([i for i in range(1, neurons_per_layer[iter_layer]+1)])
        iter_layer += 1
        
    for j in itertools.product(*layers):
        df.append(list(j))
        
    return df
    
    
    
    




def build_model(features, layers, epoch, pat):
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.callbacks import EarlyStopping
    from sklearn.metrics import accuracy_score
    
    scores = {'layers': [0, 0, 0],'accuracy': [0, 0, 0]}
    ticker = 0
    
    early_stop = EarlyStopping(monitor='val_loss',
                               mode='min',
                               verbose=1,
                               patience= pat)
    
    if layers == 1:
        for layer1 in range(1,features + 1):
            ticker += 1
            print("""
                  
                  """*5,
                  'Testing #',
                  ticker,
                  """                                                     
                                   
                  """*5)
            model = Sequential()
            model.add(Dense(features, activation='relu'))
            model.add(Dense(layer1, activation='relu'))
            
            model.add(Dense(1, activation='sigmoid'))
            model.compile(loss='binary_crossentropy',optimizer='adam')
            
            model.fit(x=X_train,
                      y=y_train,
                      epochs= epoch,
                      validation_data=[X_test,y_test],
                      callbacks=[early_stop])
            
            predictions = model.predict_classes(X_test)
            acc = accuracy_score(y_test,predictions)
            if acc > scores['accuracy'][2]:
                scores['accuracy'][2] = acc
                scores['layers'][2] = [layer1]
            elif acc > scores['accuracy'][1]:
                scores['accuracy'][1] = acc
                scores['layers'][1] = [layer1]
            elif acc > scores['accuracy'][0]:
                scores['accuracy'][0] = acc
                scores['layers'][0] = [layer1]
        
    elif layers == 2:
        for layer1 in range(1,features + 1):
            for layer2 in range(1,features + 1):
                ticker += 1
                print("""
                      
                      """*5,
                      'Testing #',
                      ticker,
                      """                                                     
                                       
                      """*5)
                model = Sequential()
                model.add(Dense(features, activation='relu'))
                model.add(Dense(layer1, activation='relu'))
                model.add(Dense(layer2, activation='relu'))
                
                model.add(Dense(1, activation='sigmoid'))
                model.compile(loss='binary_crossentropy',optimizer='adam')
                
                model.fit(x=X_train,
                          y=y_train,
                          epochs= epoch,
                          validation_data=[X_test,y_test],
                          callbacks=[early_stop])
                
                predictions = model.predict_classes(X_test)
                acc = accuracy_score(y_test,predictions)
                if acc > scores['accuracy'][2]:
                    scores['accuracy'][2] = acc
                    scores['layers'][2] = [layer1, layer2]
                elif acc > scores['accuracy'][1]:
                    scores['accuracy'][1] = acc
                    scores['layers'][1] = [layer1, layer2]
                elif acc > scores['accuracy'][0]:
                    scores['accuracy'][0] = acc
                    scores['layers'][0] = [layer1, layer2]
        
    elif layers == 3:
        for layer1 in range(1,features + 1):
            for layer2 in range(1,features + 1):
                for layer3 in range(1,features + 1):
                    ticker += 1
                    print("""
                          
                          """*5,
                          'Testing #',
                          ticker,
                          """                                                     
                                           
                          """*5)
                    model = Sequential()
                    model.add(Dense(features, activation='relu'))
                    model.add(Dense(layer1, activation='relu'))
                    model.add(Dense(layer2, activation='relu'))
                    model.add(Dense(layer3, activation='relu'))
                    
                    model.add(Dense(1, activation='sigmoid'))
                    model.compile(loss='binary_crossentropy',optimizer='adam')
                    
                    model.fit(x=X_train,
                              y=y_train,
                              epochs= epoch,
                              validation_data=[X_test,y_test],
                              callbacks=[early_stop])
                    
                    predictions = model.predict_classes(X_test)
                    acc = accuracy_score(y_test,predictions)
                    if acc > scores['accuracy'][2]:
                        scores['accuracy'][2] = acc
                        scores['layers'][2] = [layer1, layer2, layer3]
                    elif acc > scores['accuracy'][1]:
                        scores['accuracy'][1] = acc
                        scores['layers'][1] = [layer1, layer2, layer3]
                    elif acc > scores['accuracy'][0]:
                        scores['accuracy'][0] = acc
                        scores['layers'][0] = [layer1, layer2, layer3]
        
    elif layers == 4:
        for layer1 in range(1,features + 1):
            for layer2 in range(1,features + 1):
                for layer3 in range(1,features + 1):
                    for layer4 in range(1,features + 1):
                        ticker += 1
                        print("""
                              
                              """*5,
                              'Testing #',
                              ticker,
                              """                                                     
                                               
                              """*5)
                        model = Sequential()
                        model.add(Dense(features, activation='relu'))
                        model.add(Dense(layer1, activation='relu'))
                        model.add(Dense(layer2, activation='relu'))
                        model.add(Dense(layer3, activation='relu'))
                        model.add(Dense(layer4, activation='relu'))
                        
                        model.add(Dense(1, activation='sigmoid'))
                        model.compile(loss='binary_crossentropy',optimizer='adam')
                        
                        model.fit(x=X_train,
                                  y=y_train,
                                  epochs= epoch,
                                  validation_data=[X_test,y_test],
                                  callbacks=[early_stop])
                        
                        predictions = model.predict_classes(X_test)
                        acc = accuracy_score(y_test,predictions)
                        if acc > scores['accuracy'][2]:
                            scores['accuracy'][2] = acc
                            scores['layers'][2] = [layer1, layer2, layer3, layer4]
                        elif acc > scores['accuracy'][1]:
                            scores['accuracy'][1] = acc
                            scores['layers'][1] = [layer1, layer2, layer3, layer4]
                        elif acc > scores['accuracy'][0]:
                            scores['accuracy'][0] = acc
                            scores['layers'][0] = [layer1, layer2, layer3, layer4]
        
    elif layers == 5:
        for layer1 in range(1,features + 1):
            for layer2 in range(1,features + 1):
                for layer3 in range(1,features + 1):
                    for layer4 in range(1,features + 1):
                        for layer5 in range(1,features + 1):
                            ticker += 1
                            print("""
                                  
                                  """*5,
                                  'Testing #',
                                  ticker,
                                  """                                                     
                                                   
                                  """*5)
                            model = Sequential()
                            model.add(Dense(features, activation='relu'))
                            model.add(Dense(layer1, activation='relu'))
                            model.add(Dense(layer2, activation='relu'))
                            model.add(Dense(layer3, activation='relu'))
                            model.add(Dense(layer4, activation='relu'))
                            model.add(Dense(layer5, activation='relu'))
                            
                            model.add(Dense(1, activation='sigmoid'))
                            model.compile(loss='binary_crossentropy',optimizer='adam')
                            
                            model.fit(x=X_train,
                                      y=y_train,
                                      epochs= epoch,
                                      validation_data=[X_test,y_test],
                                      callbacks=[early_stop])
                            
                            predictions = model.predict_classes(X_test)
                            acc = accuracy_score(y_test,predictions)
                            if acc > scores['accuracy'][2]:
                                scores['accuracy'][2] = acc
                                scores['layers'][2] = [layer1, layer2, layer3, layer4, layer5]
                            elif acc > scores['accuracy'][1]:
                                scores['accuracy'][1] = acc
                                scores['layers'][1] = [layer1, layer2, layer3, layer4, layer5]
                            elif acc > scores['accuracy'][0]:
                                scores['accuracy'][0] = acc
                                scores['layers'][0] = [layer1, layer2, layer3, layer4, layer5]
    
    return scores, ticker

