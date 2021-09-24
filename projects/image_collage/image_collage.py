"""
Author: Ethan Nelson
File: collage_generator.py
Description: 
    Using OpenCV to constuct a collage.
    Border color, rotation and placement are randomly generated

"""
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from app import app

import numpy as np
from cv2 import cv2
import base64
from itertools import chain
import plotly.express as px

# global
images = []
image_names = []

'''
LAYOUT
'''
layout = html.Div([
    
    # row1
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    html.H1('Collage Generator', className='title'),
                    # dbc.NavLink("View on Github", active=True, href="https://github.com/einelson/BYU-I/blob/main/Computer%20vision/collage_generator.py"),
                    html.P('Collage generator is a pseudo random way to create collages. You can specify what you would like for the border, rotation and size. This is a basic creator but was a very fun project. You can add in as many pictures as you would like.', className='paragraph'),
                    html.P('The image to the right was composed of around 28 photos and has a final size of 3000 x 3000 pixels.', className='paragraph'),
                    html.P('The image generated will have a little bit of green on the border due to pixelation.', className='paragraph'),
                    html.P('To download the image press the camera button on the toolbar where your collage has been generated.', className='paragraph')
                ],
            ),
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/data/collage_generator/Nelson4.png'), className='image'),
                ],
            ),            
        ],
    ),
    # row2
    dbc.Row(
        [
            # tools
            dbc.Col(
                [
                    dbc.Card(
                        [   
                            # header
                            dbc.CardHeader('Image settings'),
                            # settings
                            dbc.CardBody(
                                [
                                    # get border
                                    html.P('Border options', className='input_line'),
                                    dcc.RadioItems(
                                        options=[  
                                            {'label': 'No border', 'value': 'no_border'},
                                            {'label': 'Random border', 'value': 'random'},
                                        ],
                                        id='in_border_color',
                                        value='random',
                                        labelStyle={'display': 'block'},
                                        style={'width':'100%'}
                                    ),


                                    # rotation 
                                    html.P('Max and Min rotation', className='input_line'),
                                    dcc.RangeSlider(
                                        id='in_rotation_slider',
                                        allowCross=False,
                                        updatemode='drag',
                                        min=-180,
                                        max=180,
                                        step=1,
                                        value=[-180,180],
                                    ),
                                    html.Div(id='out_rotation_slider'),


                                    # upload images
                                    html.P('Upload images', className='input_line'),
                                    html.Div(className='images_list'),
                                    html.Div(id='output-image-upload'),
                                    dcc.Upload(
                                        id='upload-image',
                                        children=html.Div([
                                            'Drag and Drop or ',
                                            html.A('Select Files')
                                        ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px'
                                        },
                                        # Allow multiple files to be uploaded
                                        multiple=True
                                    ),

                                    # clear uploaded
                                    dbc.Button('Clear', color='secondary', id='b_clear_uploaded'),
                                ],
                            ),

                            # execute
                            dbc.CardFooter(
                                [
                                    dbc.Button('Create', color='success', id='b_create_collage'),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            # picture output
            dbc.Col(
                [
                    dcc.Graph(id='out_image_collage', className='image_gen'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),
], className='layout')


'''
CALLBACKS
'''
# slider
@app.callback(
    Output('out_rotation_slider', 'children'),
    [Input('in_rotation_slider', 'value')])
def update_output(value):
    return ('You have chosen to rotate from ' + str(value[0]) + ' to ' + str(value[1]))


# uploaded images
def read_image_string(contents):
   encoded_data = contents[0].split(',')[1]
   nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   return img

@app.callback(
    Output('output-image-upload', 'children'),
    Input('b_clear_uploaded', 'n_clicks'),
    Input('upload-image', 'contents'),
    State('upload-image', 'filename'),
    State('upload-image', 'last_modified'))
def update_output(n, list_of_contents, list_of_names, list_of_dates):
    triggered = [p['prop_id'].split('.')[0] for p in dash.callback_context.triggered]
    
    if 'upload-image' in triggered:
        global images
        images.append(read_image_string(list_of_contents))
        global image_names
        image_names.append(list_of_names)
        return list(chain.from_iterable(image_names))
    
    else: # clear images on new page or refresh or clear
        images = []
        image_names = []

# on execute
@app.callback(
    Output('out_image_collage', 'figure'),
    Input('b_create_collage', 'n_clicks'),
    State('in_border_color','value'),
    State('in_rotation_slider','value'),
)
def make_collage(n, border, rotation):
    triggered = [p['prop_id'].split('.')[0] for p in dash.callback_context.triggered]
    if 'b_create_collage' in triggered:
        global images
        # make sure everything is filled out
        if images == []:
            return 'Upload some images'

        collage = px.imshow(main(images, border, rotation), title='Image Collage')
        collage.update_layout(paper_bgcolor = 'rgb(34, 34, 34)', font = {'color': "white", 'family': "Arial"})

        return collage
    else:
        img = np.arange(100).reshape((10, 10))
        fig = px.imshow(img, binary_string=True, title='Image Collage')
        fig.update_layout(paper_bgcolor = 'rgb(34, 34, 34)', font = {'color': "white", 'family': "Arial"})
        return fig


'''
ROTATE IMAGE
Rotates the image the degreese that is passed in
https://stackoverflow.com/questions/43892506/opencv-python-rotate-image-without-cropping-sides/47248339
'''
def rotateImage(mat, angle):
    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix. Make the background green for the green screen
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h), borderMode=cv2.BORDER_CONSTANT, borderValue=(0,255,0))
    return rotated_mat

'''
ADD BORDER
Adds a border to the image
'''
def add_border(image, color=[0,0,0]):
    image = cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=color)
    return image

'''
PLACE IMAGE
Places the image into our final image
'''
def place_image(master, image):
    height,width = image.shape[:2]

    # randomly generated position
    offsetx = np.random.randint(0, 1000)
    offsety = np.random.randint(0, 1000)

    for r in range(height):
        for c in range(width):
            try:
                b, g, red = image[r, c]
                # remove green screen
                if (b > 0) and (g != 250 ) and (red != 0):
                    master[offsetx + r, offsety + c] = image[r, c]
            except:
                pass  

    return master

def main(images, border, rotation):
    """ Main function """
    # init master image
    master=np.zeros((1500, 1500, 3), dtype=None)
    
    for image in images:

        # resize
        image = cv2.resize(image, (0,0), fx=.1, fy=.1)

        # add border
        if border == 'no_border':
            pass
        else:
            color = [np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)]
            image = add_border(image, color)

        # randomly rotate image
        deg = np.random.randint(rotation[0], rotation[1])
        image = rotateImage(image, deg)

        # place image
        master = place_image(master, image)

    return master
        

