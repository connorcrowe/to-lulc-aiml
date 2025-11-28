def build_unet(input_shape, num_classes):
    from tensorflow.keras import layers, models
    inputs = layers.Input(input_shape)
    
    # Encoder
    c1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
    c1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(c1)
    p1 = layers.MaxPooling2D((2,2))(c1)
    
    c2 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(p1)
    c2 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(c2)
    p2 = layers.MaxPooling2D((2,2))(c2)
    
    # Bottleneck
    bn = layers.Conv2D(256, (3,3), activation='relu', padding='same')(p2)
    bn = layers.Conv2D(256, (3,3), activation='relu', padding='same')(bn)
    
    # Decoder
    u2 = layers.UpSampling2D((2,2))(bn)
    u2 = layers.concatenate([u2, c2])
    c3 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(u2)
    c3 = layers.Conv2D(128, (3,3), activation='relu', padding='same')(c3)
    
    u1 = layers.UpSampling2D((2,2))(c3)
    u1 = layers.concatenate([u1, c1])
    c4 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(u1)
    c4 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(c4)
    
    outputs = layers.Conv2D(num_classes, (1,1), activation='softmax')(c4)
    model = models.Model(inputs=inputs, outputs=[outputs])
    
    return model

#def dice_coefficient(y_true, y_pred, smooth=1e-6):
#    y_true_f = K.flatten(y_true)
#    y_pred_f = K.flatten(y_pred)
#    intersection = K.sum(y_true_f * y_pred_f)
#    return (2.0 * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)