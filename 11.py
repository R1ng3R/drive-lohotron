import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import cv2
import numpy as np

logging.basicConfig(level=logging.INFO)

TOKEN = '7523890415:AAHku3FZAbQmxs8uxj4DgT_AAyobgcJZx_8'  # Replace with your bot's API token

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! Send me two images to compare.')

def compare_images(update, context):
    if len(context.bot.get_updates(offset=update.update_id - 1, timeout=100)) < 2:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Please send two images.')
        return

    file_id1 = context.bot.get_updates(offset=update.update_id - 1, timeout=100)[0].message.photo[-1].file_id
    file_id2 = context.bot.get_updates(offset=update.update_id - 2, timeout=100)[0].message.photo[-1].file_id

    file1 = context.bot.get_file(file_id1)
    file2 = context.bot.get_file(file_id2)

    img1 = cv2.imdecode(np.frombuffer(file1.download_as_bytearray(), np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(file2.download_as_bytearray(), np.uint8), cv2.IMREAD_COLOR)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    corners1 = cv2.cornerHarris(gray1, 2, 3, 0.04)
    corners2 = cv2.cornerHarris(gray2, 2, 3, 0.04)

    corners1 = cv2.normalize(corners1, None, 0, 255, cv2.NORM_MINMAX)
    corners2 = cv2.normalize(corners2, None, 0, 255, cv2.NORM_MINMAX)

    thresh = 0.01
    corner_points1 = np.where(corners1 > thresh * corners1.max())
    corner_points2 = np.where(corners2 > thresh * corners2.max())

    img1_corners = img1.copy()
    img2_corners = img2.copy()
    for point in zip(*corner_points1[::-1]):
        cv2.circle(img1_corners, point, 3, (0, 0, 255), -1)
    for point in zip(*corner_points2[::-1]):
        cv2.circle(img2_corners, point, 3, (0, 0, 255), -1)

    corner_points1 = np.array(corner_points1).T
    corner_points2 = np.array(corner_points2).T

    distances = np.linalg.norm(corner_points1[:, None] - corner_points2[None, :], axis=2)
    min_distances = np.min(distances, axis=1)
    avg_min_distance = np.mean(min_distances)

    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Average minimum distance between corner points: {avg_min_distance:.2f}')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.photo, compare_images))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()